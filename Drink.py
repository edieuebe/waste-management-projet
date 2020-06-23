from Cans import Can
from Bottles import Bottles

class Drink():
    def __init__(self, name, cases, bottled):
        self.name = name
        self.cases = cases
        self.bottled = bottled
        if bottled:
            self.packaging_waste = Bottles(cases)
        else:
            self.packaging_waste = Can(cases)

        self.totalDrinkWaste = self.drinkWaste()

    def drinkWaste(self):
        packagingWaste  = self.packaging_waste.totalWaste
        ingredientWaste = self.Sugar_Citric_NaBenz_Bags()
        return packagingWaste + ingredientWaste

    def sugar_citric_calc(self, gallons, constant):
        return round((gallons*constant)/50 )

    def sodium_benzonate_calc(self, gallons, constant):
        return round((gallons*constant)/55)

    def Sugar_Citric_NaBenz_Bags(self):
        #from the expected case quantity, we can determine the total gallons of product being produced

        #initialize volume 
        V_sugar      = 0.0029502 #m^3
        V_citric     = 0.0029502 #m^3
        V_sodiumbenz = 0.0029502 # STILL need to find this value (placeholder right now)
        V_quinine    = 0
        V_phosphoric = 0

        #determine quantities 
        gallons = self.cases*2.25
        if self.name == 'Margarita' :
            sugar           = self.sugar_citric_calc(gallons, 0.63493132)#50lb bags
            citric          = self.sugar_citric_calc(gallons, 0.04703195)#50lb bags
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00383192) #55lb bags
            quinine         = 0
            phosphoric_acid = 0

        elif self.name == 'Mai Tai':
            sugar           = self.sugar_citric_calc(gallons, 0.56533333)
            citric          = self.sugar_citric_calc(gallons, 0.0235111)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0013713333333333)
            quinine         = 0
            phosphoric_acid = 0

        elif self.name == 'Gin Tonic':
            sugar           = self.sugar_citric_calc(gallons, 0.638582716049382)
            citric          = self.sugar_citric_calc(gallons, 0.0269177777777778)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0014318)
            quinine         = 0
            phosphoric_acid = 0

        elif self.name == 'Mojito':
            sugar           = self.sugar_citric_calc(gallons, 0.2822444)
            citric          = self.sugar_citric_calc(gallons, 0.02)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00282192)
            quinine         = 0
            phosphoric_acid = 0

        elif self.name == 'Paloma':
            sugar           = self.sugar_citric_calc(gallons, 0.423287543)
            citric          = self.sugar_citric_calc(gallons, 0.01316895)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.00282192)
            quinine         = 0
            phosphoric_acid = 0

        elif self.name=='Rum Cola':
            sugar           = self.sugar_citric_calc(gallons, 0.65844729)
            citric          = self.sugar_citric_calc(gallons, 0.0006608)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.001475)
            quinine         = 0
            phosphoric_acid = 0 #find out size of this bag , there is a quantity here

        elif self.name=='Rum Ginger':
            sugar           = self.sugar_citric_calc(gallons, 0.541676543209876)
            citric          = self.sugar_citric_calc(gallons, 0.010285012345679)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.013713333333333)
            quinine         = 0
            phosphoric_acid = 0

        elif self.name=='Tequila Soda':
            sugar           = 0
            citric          = 0
            sodium_benzoate = 0
            quinine         = 0
            phosphoric_acid = 0

        elif self.name=='Vodka Mule':
            sugar           = self.sugar_citric_calc(gallons, 0.541676543209876)
            citric          = self.sugar_citric_calc(gallons, 0.010285012345679)
            sodium_benzoate = self.sodium_benzonate_calc(gallons, 0.0013713333333333)
            quinine         = 0
            phosphoric_acid = 0

        else:
            sugar           = 0
            citric          = 0
            sodium_benzoate = 0
            quinine         = 0
            phosphoric_acid = 0

        kettle_waste = (sugar*V_sugar)+(citric*V_citric)+(sodium_benzoate*V_sodiumbenz)+(quinine*V_quinine)+(phosphoric_acid*V_phosphoric)

        return kettle_waste