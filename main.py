#!/usr/local/bin/python3

from Drink import Drink
import csv
import os
import sys
from Cans import Can

def usage(exit_code = 0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-s DRINKNAME -i PATH]
    -n "DRINK NAME" Singular drink data, pass the name as "DRINK NAME", dont forget quotes
    -i PATH         Specify path to data file (default drink-setup.txt)
    -d DAYS         Specify number of days to do calculations for (default 1)''')
    sys.exit(exit_code)

def getTotalDayWaste(drinks):
    totalWaste = 0
    for drink in drinks.values():
        totalWaste += drink.totalDrinkWaste

    return totalWaste

def getTotalDayCases(drinks):
    totalCases = 0
    for drink in drinks.values():
        totalCases += drink.cases

    return totalCases

def getTotalDayVolumetric(drinks):
    totalVolumetric = 0
    for drink in drinks.values():
        totalVolumetric += drink.totalSolidWaste

    return totalVolumetric

def printDailyTable(drinks, days):
    print('')
    print(f'Drink Name        Cases    Liquid volumetric waste (m^3)  Total volumetric waste w/ 15% excluded volume (m^3)')
    
    for drink in drinks.values():
        print('-------------------------------------------------------------------------------------------------------------')
        print(f'{drink.name:<17}  {drink.cases*days:<15} {drink.totalDrinkWaste*days:<40} {drink.totalSolidWaste*days}')

    totalStr = f'Total for {days} days'
    print('-------------------------------------------------------------------------------------------------------------')
    print(f'{totalStr:<18} {getTotalDayCases(drinks)*days:<15} {getTotalDayWaste(drinks)*days:<40} {getTotalDayVolumetric(drinks)*days}')
    print('-------------------------------------------------------------------------------------------------------------')
    print('')

def printSingleDrink(drink, days):
    print('')
    print(f'{drink.name:>4} : {drink.cases} cases = {drink.totalDrinkWaste} m^3 of liquid volumetric waste')
    print(f'{drink.name:>4} : {drink.cases} cases = {drink.totalDrinkWaste+(0.15*3.126)} m^3 of total volumetric waste assuming 15% excluded volume')
    print('')
# Main function
def main():

    # initialize default values
    arguments = sys.argv[1:]
    single = False
    path = 'drink-setup.txt'
    specificDrink = 'None'
    days = 1

    # Loop through arguments to parse
    while len(arguments) and arguments[0].startswith('-'):
        arg = arguments.pop(0)
        if arg == '-i':
            path = arguments.pop(0)
        elif arg == '-n':
            single = True
            specificDrink = arguments.pop(0)
        elif arg == '-d':
            days = int(arguments.pop(0))
        elif arg == '-h':
            usage()
        else:
            usage(1)

    # Open and get csv object from file
    csv_reader = csv.reader(open(path, 'r'))

    # Dictionary comprehension of form {key:value for [name, cases, bottled, efficiency] in csvfile}
    # Creates drink objects for each line in csv file

    drinks = {line[0]:Drink(line[0], int(line[1]), line[2], int(line[3])) for line in csv_reader}

    if single == False:
        printDailyTable(drinks, days)
    else:
        printSingleDrink(drinks.get(specificDrink), days)
    #total =0
    #for i in range(len(drinks)):
        #total += drink.totalDrinkWaste[i]+(0.15*3.126)
        #i+=1
        #return total
        #print('The total amount of volumetric waste for this time prediod is: ', total)

if __name__ == '__main__':
    main()
