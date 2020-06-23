#!/usr/local/bin/python3

from Drink import Drink
import csv
import os

def usage(exit_code = 0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-s DRINKNAME -i PATH]
    -s DRINKNAME Singular drink data, pass the name as DRINKNAME
    -i PATH      Specify path to data file (default drink-setup.txt)''')
    sys.exit(exit_code)

def main():
    csv_reader = csv.reader(open('drink-setup.txt', 'r'))

    # Dictionary comprehension of form {key:value for [name, cases, bottled] in csvfile}
    drinks = {line[0]:Drink(line[0], line[1], line[2]) for line in csv_reader}

    for drink in drinks.values():
       print(f'{drink.name} : {drink.cases}')

if __name__ == '__main__':
    main()