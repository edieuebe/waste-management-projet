#!/usr/local/bin/python3

from Drink import Drink
import csv
import os
import sys
from Cans import Can
import tkinter as tk
from tkinter import *

def usage(exit_code = 0):
    progname = os.path.basename(sys.argv[0])
    print(f'''Usage: {progname} [-s DRINKNAME -i PATH]
    -n "DRINK NAME" Singular drink data, pass the name as "DRINK NAME", dont forget quotes
    -i PATH         Specify path to data file (default drink-setup.txt)
    -d DAYS         Specify number of days to do calculations for (default 1)
    -g              Run Program with GUI''')
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

def getTotalTonnage(drinks):
    totalTonnage = 0
    for drink in drinks.values():
        totalTonnage += drink.totalTonnage

    return totalTonnage

def updateDataFrame(root, drinks, drinkNameInput, drinkCaseInput):
    drinkName = drinkNameInput.get()
    cases = int(drinkCaseInput.get())

    try:
        drinks.get(drinkName).cases = cases
    except:
        print("Unable to find drink")

    createDrinkFrame(root, drinks)
    createDataFrame(root, drinks)

def createDrinkFrame(root, drinks):
    addDrinkFrame = tk.Frame(root, bg="#4e9686")
    addDrinkFrame.place(relwidth=0.3, relheight=0.4, relx=0.01, rely=0.02)

    drinkFrameLabel = tk.Label(addDrinkFrame, text="Update Cases", bg="#4e9686", fg="black")
    drinkFrameLabel.grid(row=0, column=0, columnspan=2, pady=40, padx=10)

    drinkNameEntryLabel = tk.Label(addDrinkFrame, text="Drink Name", bg="#4e9686", fg="white")
    drinkNameEntryLabel.grid(row=1, column=0, pady=10, padx=10)

    drinkNameInput = tk.Entry(addDrinkFrame, width=15, bg="white")
    drinkNameInput.grid(row=1, column=1, padx=10)

    drinkCaseEntryLabel = tk.Label(addDrinkFrame, text="Cases", bg="#4e9686", fg="white")
    drinkCaseEntryLabel.grid(row=2, column=0, pady=10, padx=10)

    drinkCaseInput = tk.Entry(addDrinkFrame, width=15, bg="white")
    drinkCaseInput.grid(row=2, column=1, padx=10)

    changeDrinkButton = tk.Button(addDrinkFrame, width=10, text="Update", highlightbackground="black", bd=0, fg="white", command=lambda: updateDataFrame(root, drinks, drinkNameInput, drinkCaseInput))
    changeDrinkButton.grid(row=3, column=0, columnspan=2, pady=10)

def createDataFrame(root, drinks):
    colwidth = 11

    addDataFrame = tk.Frame(root, bg="#4e9686")
    addDataFrame.place(relwidth=0.67, relheight=0.96, relx=0.32, rely=0.02)

    nameDataLabel = tk.Label(addDataFrame, text="Drink Name", bg="#4e9686", fg="black", anchor="w", width=15)
    nameDataLabel.grid(row=0, column=0, padx=10, pady=10)

    caseDataLabel = tk.Label(addDataFrame, text="Cases", bg="#4e9686", fg="black", anchor="w", width=colwidth)
    caseDataLabel.grid(row=0, column=1, padx=10, pady=10)

    volumetricDataLabel = tk.Label(addDataFrame, text="Liquid Volumetric\nWaste (m^3)", bg="#4e9686", fg="black", anchor="w", width=colwidth)
    volumetricDataLabel.grid(row=0, column=2, padx=10, pady=10)

    totalDataLabel = tk.Label(addDataFrame, text=" Solid Volumetric\nWaste (m^3)", bg="#4e9686", fg="black", anchor="w", width=colwidth)
    totalDataLabel.grid(row=0, column=3, padx=10, pady=10)

    solidDataLabel = tk.Label(addDataFrame, text="Total \nWeight (Tons)", bg="#4e9686", fg="black", anchor="w", width=colwidth)
    solidDataLabel.grid(row=0, column=4, padx=10, pady=10)

    for i, drink in enumerate(drinks.values(), start=1):
        drinkNameDataLabel = tk.Label(addDataFrame, text=drink.name, bg="#4e9686", fg="white", anchor="w", width=15)
        drinkNameDataLabel.grid(row=i, column=0, padx=10, pady=5)

        drinkCasesDataLabel = tk.Label(addDataFrame, text=str(drink.cases), bg="#4e9686", fg="white", anchor="w", width=colwidth)
        drinkCasesDataLabel.grid(row=i, column=1, padx=10, pady=5)

        drinkLiquidVolumetricLabel = tk.Label(addDataFrame, text=str(round(drink.totalDrinkWaste, 3)), bg="#4e9686", fg="white", width=colwidth)
        drinkLiquidVolumetricLabel.grid(row=i, column=2, padx=10, pady=5)

        drinkTotalVolumetricLabel = tk.Label(addDataFrame, text=str(round(drink.totalSolidWaste, 3)), bg="#4e9686", fg="white", width=colwidth)
        drinkTotalVolumetricLabel.grid(row=i, column=3, padx=10, pady=5)

        drinkTotalSolidLabel = tk.Label(addDataFrame, text=str(round(drink.totalTonnage, 3)), bg="#4e9686", fg="white", width=colwidth)
        drinkTotalSolidLabel.grid(row=i, column=4, padx=10, pady=5)

def runWithGUI(drinks):

    bottled = False

    root = Tk()
    root.title("Drink and Waste Production")

    canvas = tk.Canvas(root, height=700, width=1000, bg="#21bf4b")
    canvas.pack()

    createDrinkFrame(root, drinks)
    createDataFrame(root, drinks)

    root.mainloop()


def printDailyTable(drinks, days):
    print('')
    print(f'Drink Name            Cases         Liquid volumetric waste (m^3)      Total volumetric waste w/ 10% excluded volume (m^3)    Total Weight(Tons) ')
    
    for drink in drinks.values():
        print('-------------------------------------------------------------------------------------------------------------------------------------------------')
        print(f'{drink.name:<20}  {drink.cases*days:<18} {drink.totalDrinkWaste*days:<45} {drink.totalSolidWaste*days:<38} {drink.totalTonnage}')
    if days > 1:
        totalStr = f'Total for {days} days'
    else:
        totalStr = 'Total'
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print(f'{totalStr:<20} {getTotalDayCases(drinks)*days:<18} {getTotalDayWaste(drinks)*days:<45} {getTotalDayVolumetric(drinks)*days:<38} {getTotalTonnage(drinks)*days}')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    print('')

def printSingleDrink(drink, days):
    print('')
    print(f'{drink.name} : {drink.cases} cases = {drink.totalDrinkWaste} m^3 of liquid volumetric waste')
    print(f'{drink.name} : {drink.cases} cases = {drink.totalDrinkWaste+(0.15*3.126)} m^3 of total volumetric waste assuming 15% excluded volume')
    print('')
# Main function
def main():

    # initialize default values
    arguments = sys.argv[1:]
    single = False
    path = 'drink-setup.txt'
    specificDrink = 'None'
    days = 1
    withGUI = False

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
        elif arg == '-g':
            withGUI = True
        elif arg == '-h':
            usage()
        else:
            usage(1)

    # Open and get csv object from file
    csv_reader = csv.reader(open(path, 'r'))

    # Dictionary comprehension of form {key:value for [name, cases, bottled, efficiency] in csvfile}
    # Creates drink objects for each line in csv file

    drinks = {line[0]:Drink(line[0], int(line[1]), line[2], int(line[3])) for line in csv_reader}

    if withGUI:
        runWithGUI(drinks)
    else:
        if single == False:
            printDailyTable(drinks, days)
        else:
            printSingleDrink(drinks.get(specificDrink), days)

if __name__ == '__main__':
    main()
