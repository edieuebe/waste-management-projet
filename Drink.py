from Cans import Can
from Bottles import Bottles

class Drink():
    def __init__(self, name, cases, bottled, efficiency):
        self.name = name
        self.cases = cases
        self.efficiency = efficiency #this is defined as decimal value in other functions
        self.bottled = bottled

        if (self.bottled):
            self.packaging_waste = Bottles(cases, efficiency)
        else:
            self.packaging_waste = Can(cases, efficiency)

        self.totalDrinkWaste = self.drinkWaste()
        self.totalSolidWaste = self.totalDrinkWaste+(0.10*3.126)
        self.totalTonnage = self.totalDrinkWaste*(1.09351**3)*106*0.0005 #weight of waste in tons for corrogated cardboard

    def updateCaseData(self, cases):
        self.cases = cases
        if (self.bottled):
            self.packaging_waste = Bottles(self.cases, self.efficiency)
        else:
            self.packaging_waste = Can(self.cases, self.efficiency)

        self.totalDrinkWaste = self.drinkWaste()
        self.totalSolidWaste = self.totalDrinkWaste+(0.10*3.126)
        self.totalTonnage = self.totalDrinkWaste*(1.09351**3)*106*0.0005 #weight of waste in tons for corrogated cardboard

    def drinkWaste(self):
        packagingWaste  = self.packaging_waste.totalWaste
        #print(packagingWaste)
        ingredientWaste = self.Sugar_Citric_NaBenz_Bags()
        #print(ingredientWaste)
        return packagingWaste + ingredientWaste

    def sugar_citric_calc(self, gallons, constant):
        return round((gallons*constant)/50)

    def sodium_benzonate_calc(self, gallons, constant):
        return round((gallons*constant)/55)

    def Sugar_Citric_NaBenz_Bags(self):
        #from the expected case quantity, we can determine the total gallons of product being produced

        #initialize volume 
        V_sugar      = 0.0029502 #m^3
        V_citric     = 0.0029502 #m^3
        V_sodiumbenz = 0.003124 #high key guessed 

        #determine quantities 
        gallons = self.cases*2.25
        if self.name == 'Margarita' :
            sugar           = self.sugar_citric_calc(gallons, 0.63493132)#50lb bags
            citric          = self.sugar_citric_calc(gallons, 0.04703195)#50lb bags
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00383192) #55lb bags

        elif self.name == 'Mai Tai':
            sugar           = self.sugar_citric_calc(gallons, 0.56533333)
            citric          = self.sugar_citric_calc(gallons, 0.0235111)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0013713333333333)

        elif self.name == 'Gin Tonic':
            sugar           = self.sugar_citric_calc(gallons, 0.638582716049382)
            citric          = self.sugar_citric_calc(gallons, 0.0269177777777778)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0014318)

        elif self.name == 'Mojito':
            sugar           = self.sugar_citric_calc(gallons, 0.2822444)
            citric          = self.sugar_citric_calc(gallons, 0.02)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00282192)

        elif self.name == 'Paloma':
            sugar           = self.sugar_citric_calc(gallons, 0.423287543)
            citric          = self.sugar_citric_calc(gallons, 0.01316895)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00282192)

        elif self.name=='Rum Cola':
            sugar           = self.sugar_citric_calc(gallons, 0.65844729)
            citric          = self.sugar_citric_calc(gallons, 0.0006608)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.001475)

        elif self.name=='Rum Ginger':
            sugar           = self.sugar_citric_calc(gallons, 0.541676543209876)
            citric          = self.sugar_citric_calc(gallons, 0.010285012345679)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.013713333333333)

        elif self.name=='Vodka Mule':
            sugar           = self.sugar_citric_calc(gallons, 0.541676543209876)
            citric          = self.sugar_citric_calc(gallons, 0.010285012345679)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0013713333333333)

        elif self.name=='Whiskey Mule':
            sugar           = self.sugar_citric_calc(gallons, 0.47031949)
            citric          = self.sugar_citric_calc(gallons, 0.01011187)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0013713333333333)

        elif self.name=='Horchata Cold Brew':
            sugar           = self.sugar_citric_calc(gallons, 0.470318933)
            citric          = 0
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.002121914)

        elif self.name=='Elderflower Spritz':
            sugar           = self.sugar_citric_calc(gallons, 0.282191111111111)
            citric          = self.sugar_citric_calc(gallons, 0.0094059259259259)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00282192)

        else:
            sugar           = 0
            citric          = 0
            sodium_benzoate = 0

        kettle_waste = (sugar*V_sugar)+(citric*V_citric)+(sodium_benzoate*V_sodiumbenz)

        return kettle_waste
