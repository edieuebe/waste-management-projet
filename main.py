#!/usr/local/bin/python3

from Drink import Drink
import csv
import os
import sys
from Cans import Can

def usage(exit_code = 0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-s DRINKNAME -i PATH]
    -d DRINKNAME Singular drink data, pass the name as DRINKNAME
    -i PATH      Specify path to data file (default drink-setup.txt)''')
    sys.exit(exit_code)

# Main function
def main():

    # initialize default values
    arguments = sys.argv[1:]
    single = False
    path = 'drink-setup.txt'
    specificDrink = 'None'

    # Loop through arguments to parse
    while len(arguments) and arguments[0].startswith('-'):
        arg = arguments.pop(0)
        if arg == '-i':
            path = arguments.pop(0)
        elif arg == '-d':
            single = True
            specificDrink = arguments.pop(0)
        elif arg == '-h':
            usage()
        else:
            usage(1)

    # Open and get csv object from file
    csv_reader = csv.reader(open(path, 'r'))

    # Dictionary comprehension of form {key:value for [name, cases, bottled, efficiency] in csvfile}
    # Creates drink objects for each line in csv file

    drinks = {line[0]:Drink(line[0], int(line[1]), line[2], int(line[3])) for line in csv_reader}

    for drink in drinks.values():
        print('')
        print(f'{drink.name:>4} : {drink.cases} cases = {drink.totalDrinkWaste} m^3 of liquid volumetric waste')
        print(f'{drink.name:>4} : {drink.cases} cases = {drink.totalDrinkWaste+(0.15*3.126)} m^3 of total volumetric waste assuming 15% excluded volume')
        print('')

    #total =0
    #for i in range(len(drinks)):
        #total += drink.totalDrinkWaste[i]+(0.15*3.126)
        #i+=1
        #return total
        #print('The total amount of volumetric waste for this time prediod is: ', total)

if __name__ == '__main__':
    main()
