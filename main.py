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

def getTotalDrinkNames(drinks):
    totalDrinkNames=0
    for drink in enumerate(drinks.values(), start=0):
        totalDrinkNames+=1
    return (totalDrinkNames+1) #used in GUI

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

def BinAnalysis(drinks):
    #bin size is 3.058m^3
    V_bin = 3.058
    bin_percent = (getTotalDayVolumetric(drinks)/V_bin) 

    return bin_percent

def CompactorAnalysis(drinks):
    V_compactor = 39.870 #compact ratio of 6/1
    compactor_percent = (getTotalDayVolumetric(drinks)/V_compactor)/6

    return compactor_percent

def updateDataFrame(root, drinks, drinkNameInput, drinkCaseInput):
    drinkName = drinkNameInput.get()
    cases = int(drinkCaseInput.get())

    try:
        drink = drinks.get(drinkName)
    except:
        print("Unable to find drink")

    drink.updateCaseData(cases)

    createDrinkFrame(root, drinks)
    createDataFrame(root, drinks)

def createDrinkFrame(root, drinks):
<<<<<<< HEAD
    addDrinkFrame = tk.Frame(root, bg="steelblue")
    addDrinkFrame.place(relwidth=0.3, relheight=0.4, relx=0.01, rely=0.02)

    drinkFrameLabel = tk.Label(addDrinkFrame, text="Update Cases", bg="steelblue", fg="black")
    drinkFrameLabel.grid(row=0, column=0, columnspan=2, pady=40, padx=10)
=======
    addDrinkFrame = tk.Frame(root, bg="#4e9686")
    addDrinkFrame.place(relwidth=0.3, relheight=0.5, relx=0.01, rely=0.02)

    drinkFrameLabel = tk.Label(addDrinkFrame, text="Update Cases", bg="#4e9686", fg="black")
    drinkFrameLabel.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
>>>>>>> 982ae3845a2da328b0d674e3fce914ad30536f1f

    drinkNameEntryLabel = tk.Label(addDrinkFrame, text="Drink Name", bg="steelblue", fg="white")
    drinkNameEntryLabel.grid(row=1, column=0, pady=10, padx=10)

    drinkNameInput = tk.Entry(addDrinkFrame, width=15, bg="white")
    drinkNameInput.grid(row=1, column=1, padx=10)

    drinkCaseEntryLabel = tk.Label(addDrinkFrame, text="Cases", bg="steelblue", fg="white")
    drinkCaseEntryLabel.grid(row=2, column=0, pady=11, padx=10)

    drinkCaseInput = tk.Entry(addDrinkFrame, width=15, bg="white")
    drinkCaseInput.grid(row=2, column=1, padx=10)

    changeDrinkButton = tk.Button(addDrinkFrame, width=10, text="Update", highlightbackground="lightsteelblue", bd=0, fg="white", command=lambda: updateDataFrame(root, drinks, drinkNameInput, drinkCaseInput))
    changeDrinkButton.grid(row=3, column=0, columnspan=2, pady=10)

<<<<<<< HEAD
def createAnalysisFrame(root, drinks):

    addAnalysisFrame = tk.Frame(root, bg="steelblue")
    addAnalysisFrame.place(anchor = SW, relwidth=0.3, relheight=0.54, relx=0.01, rely=0.98)

    AnalysisFrameLabel = tk.Label(addAnalysisFrame, text="Analysis of Disposal Options", bg="steel blue", fg="black")
    AnalysisFrameLabel.grid(row=0, column=0, columnspan=2, pady=40, padx=50)

    AnalysisBinLabel = tk.Label(addAnalysisFrame, text="The waste fills up ", bg="steel blue", fg="white")
    AnalysisBinLabel.grid(row=3, column=0, pady=1, padx=80)

    AnalysisBin2Label = tk.Label(addAnalysisFrame, text="total recycling bins", bg="steel blue", fg="white")
    AnalysisBin2Label.grid(row=5, column=0, padx=1, pady=1)

    AnalysisCompLabel = tk.Label(addAnalysisFrame, text="With a 6/1 compact ratio", bg="steel blue", fg="white")
    AnalysisCompLabel.grid(row=6, column=0, padx=1, pady=(50,1))

    AnalysisCompLabel = tk.Label(addAnalysisFrame, text="the waste fills up", bg="steel blue", fg="white")
    AnalysisCompLabel.grid(row=7, column=0, padx=1, pady=1)

    AnalysisComp2Label = tk.Label(addAnalysisFrame, text="total compactors", bg="steel blue", fg="white")
    AnalysisComp2Label.grid(row=9, column=0, padx=1, pady=1)

    BinPercentVol = tk.Label(addAnalysisFrame, text = str(round(BinAnalysis(drinks),3)), bg="steelblue", fg="blue4", font=20)
    BinPercentVol.grid(row=4, column=0, padx=1, pady=1)

    CompPercentVol= tk.Label(addAnalysisFrame, text=str(round(CompactorAnalysis(drinks),3)), bg="steelblue", fg="blue4", font=80)
    CompPercentVol.grid(row=8, column=0, padx=1, pady=1)

=======
    newFileLabel = tk.Label(addDrinkFrame, text="New Save File", bg="#4e9686", fg="white")
    newFileLabel.grid(row=4, column=0, pady=10)

    newFileInput = tk.Entry(addDrinkFrame, width=15, bg="white")
    newFileInput.grid(row=4, column=1, pady=10)

    fileSaveInfo = tk.Label(addDrinkFrame, text="Leave blank to save to default setup file", bg="#4e9686", fg="white")
    fileSaveInfo.grid(row=5, column=0, columnspan=2, pady=10)

    saveFileButton = tk.Button(addDrinkFrame, text="Save", width=10, highlightbackground="black", bd=0, fg="white", command=lambda: saveNewCSV(drinks, newFileInput, addDrinkFrame))
    saveFileButton.grid(row=6, column=0, columnspan=2, pady=10)

def saveNewCSV(drinks, newFileInput, addDrinkFrame):
    
    if newFileInput.get() == "":
        filename = "drink-setup.txt"
    else:
        filename = newFileInput.get()

    with open(filename, 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for drink in drinks.values():
            print(drink.bottled)
            line = [drink.name, str(drink.cases), "bottled" if drink.bottled else "canned", str(drink.efficiency)]
            csv_writer.writerow(line)

    savedConfirmation = tk.Label(addDrinkFrame, text="File Saved Successfully! :)", bg="#4e9686", fg="white")
    savedConfirmation.grid(row=7, column=0, columnspan=2, pady=10)
>>>>>>> 982ae3845a2da328b0d674e3fce914ad30536f1f

def createDataFrame(root, drinks):
    colwidth = 11

    addDataFrame = tk.Frame(root, bg="steelblue")
    addDataFrame.place(relwidth=0.67, relheight=0.96, relx=0.32, rely=0.02)

    nameDataLabel = tk.Label(addDataFrame, text="Drink Name", bg="steelblue", fg="black", anchor="w", width=17)
    nameDataLabel.grid(row=0, column=0, padx=10, pady=10)

    caseDataLabel = tk.Label(addDataFrame, text="Cases", bg="steelblue", fg="black", anchor="w", width=colwidth)
    caseDataLabel.grid(row=0, column=1, padx=10, pady=10)

    volumetricDataLabel = tk.Label(addDataFrame, text="Liquid Volumetric\nWaste (m^3)", bg="steelblue", fg="black", anchor="w", width=colwidth+2)
    volumetricDataLabel.grid(row=0, column=2, padx=10, pady=10)

    totalDataLabel = tk.Label(addDataFrame, text=" Solid Volumetric\nWaste (m^3)", bg="steelblue", fg="black", anchor="w", width=colwidth+2)
    totalDataLabel.grid(row=0, column=3, padx=10, pady=10)

    solidDataLabel = tk.Label(addDataFrame, text="Total \nWeight (Tons)", bg="steelblue", fg="black", anchor="w", width=colwidth)
    solidDataLabel.grid(row=0, column=4, padx=10, pady=10)

    DrinkTotalDataTable = tk.Label(addDataFrame, text="Total: ", bg="steelblue", fg="blue4", anchor="w")
    DrinkTotalDataTable.grid(row=(getTotalDrinkNames(drinks)), column=0, padx=0, pady=0)


    for i, drink in enumerate(drinks.values(), start=1):
        drinkNameDataLabel = tk.Label(addDataFrame, text=drink.name, bg="steelblue", fg="white", anchor="w", width=15)
        drinkNameDataLabel.grid(row=i, column=0, padx=10, pady=5)

        drinkCasesDataLabel = tk.Label(addDataFrame, text=str(drink.cases), bg="steelblue", fg="white", anchor="w", width=colwidth)
        drinkCasesDataLabel.grid(row=i, column=1, padx=10, pady=5)

        drinkLiquidVolumetricLabel = tk.Label(addDataFrame, text=str(round(drink.totalDrinkWaste, 3)), bg="steelblue", fg="white", width=colwidth)
        drinkLiquidVolumetricLabel.grid(row=i, column=2, padx=10, pady=5)

        drinkTotalVolumetricLabel = tk.Label(addDataFrame, text=str(round(drink.totalSolidWaste, 3)), bg="steelblue", fg="white", width=colwidth)
        drinkTotalVolumetricLabel.grid(row=i, column=3, padx=10, pady=5)

        drinkTotalSolidLabel = tk.Label(addDataFrame, text=str(round(drink.totalTonnage, 3)), bg="steelblue", fg="white", width=colwidth)
        drinkTotalSolidLabel.grid(row=i, column=4, padx=10, pady=5)


    OverallTotalCases = tk.Label(addDataFrame, text = str(round(getTotalDayCases(drinks),3)), bg="steelblue", fg="blue4", width=colwidth)
    OverallTotalCases.grid(row=getTotalDrinkNames(drinks), column=1, padx=10, pady=10)

    OverallTotalVolumetricWaste = tk.Label(addDataFrame, text = str(round(getTotalDayVolumetric(drinks),3)), bg="steelblue", fg="blue4", width=colwidth)
    OverallTotalVolumetricWaste.grid(row=getTotalDrinkNames(drinks), column=2, padx=10, pady=10)

    OverallSolidWaste = tk.Label(addDataFrame,text=str(round(getTotalDayWaste(drinks),3)), bg="steelblue", fg="blue4", width=colwidth)
    OverallSolidWaste.grid(row=getTotalDrinkNames(drinks), column=3, padx=10, pady=10)

    OverallTonnage = tk.Label(addDataFrame, text=str(round(getTotalTonnage(drinks),3)), bg="steelblue", fg="blue4", width=colwidth)
    OverallTonnage.grid(row=getTotalDrinkNames(drinks), column=4, padx=10, pady=10)


def runWithGUI(drinks):

    bottled = False

    root = Tk()
    root.title("Drink and Waste Production")

    canvas = tk.Canvas(root, height=700, width=1040, bg="lightsteelblue")
    canvas.pack()

    createDrinkFrame(root, drinks)
    createAnalysisFrame(root, drinks)
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
    print(f'{totalStr:<20} {getTotalDayCases(drinks)*days:<18} {getTotalDayWaste(drinks)*days:<45} {getTotalDayVolumetric(drinks)*days:<39} {getTotalTonnage(drinks)*days}')
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

    drinks = {line[0]:Drink(line[0], int(line[1]), True if line[2].strip() == "bottled" else False, int(line[3])) for line in csv_reader}

    for drink in drinks.values():
        print(drink.bottled)

    if withGUI:
        runWithGUI(drinks)
    else:
        if single == False:
            printDailyTable(drinks, days)
        else:
            printSingleDrink(drinks.get(specificDrink), days)

if __name__ == '__main__':
    main()
