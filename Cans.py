class Can():
    def __init__(self, name, cases):
        self.name           = name #should be applied to specific drink 
        self.cases          = cases #number of cases being produced
        self.num_cans       = cases*4*6 # 6 cartons per case, 4 cans per carton

    def Lids(self, cases, num_cans):
        # each pallet contains 351,654 lids
        # every pallet has three large, thick cardboard sheets holding it in place
        # each row on pallet contains 22 slips (each with 552 lids inside) wrapped in a thin cardboard sheet
        
        #initialize volumes
        V_lid      = 4.867e-4 #m^3
        V_slip     = 5.9004e-4 #m^3
        V_slipwrap = 5.9004e-4 #m^3
        V_palletCB = 3*0.0230 #m^3
        
        #define quantities
        lids          = num_cans *4*6
        slips         = lids/552 # there are 552 lids per slip; each slip goes to recyclinig
        L_pallet_rows = slips/22 #there are 22 slips per row on pallet; splitting each row is a large cardboard sheet (wraps around the 22 slips to hold in place)
        num_pallets   = num_cans / 351,654
        trashed_lids  = lids*0.01 #assume 99% efficiency

        #determine waste volume from lid waste
        V_Lid_waste = (V_lid*trashed_lids)+(slips*V_slip)+(V_slipwrap*L_pallet_rows)+(V_palletCB*num_pallets)
        
        return V_Lid_waste

    def Cartons(self, cases):
        # each pallet contains 24 boxes (4 rows of 6 boxes)
        # There is a large cardboard sheet seperating each row and a cardboard slip on the bottom of each pallet
        # there are 275 cartons in each box, each box is recycled

        # initialize volumes
        V_lidperrow_broken     = 0.0162 #m^3 #this is the CB lid seperating each row on pallet # volume of it broken down
        V_lidperrow_NOT_broken = 0.0904 #m^3 #volume if it is not broken down
        V_pallet_slipsheet     = 0.0230 #m^3 #CB on bottom of each pallet
        V_cartonbox            = 0.00608 #m^3 # always broken down boxes
        V_carton_broken        = 1.024e-4 #m^3
        V_carton_notbroken     = 0.00273 #m^3

        #define quantities
        num_cartons     = cases*6
        carton_box      = num_cartons/275 #all boxes are broken down and recycled
        CT_pallet_rows  = carton_box/6 #6 boxes on each row
        num_pallets     = CT_pallet_rows/4 
        trashed_cartons = num_cartons+0.01 #assume 99% efficiency 

        # determine waste volume from carton waste
        #assume 90% of the boxes are broken down, 10% not broken down
        V_CB_rowlids   = ((CT_pallet_rows*0.90)*V_lidperrow_broken) +((CT_pallet_rows*0.10)*V_lidperrow_NOT_broken)
        V_cartons      = ((trashed_cartons*0.90)*V_carton_broken)+((trashed_cartons*0.10)*V_carton_notbroken)
        V_carton_waste = V_CB_rowlids +V_cartons + (carton_box *V_cartonbox)+(num_pallets*V_pallet_slipsheet)

        return V_carton_waste

    def Trays (self, cases):
        #each pallet contains 2400 flat trays 
        #on each pallet, there are 2 a large thick cardboard covers and 2 slipsheets on the bottom of pallet

        #initialize volumes 
        V_pallet_covers  = 2*0.0137 #m^3
        V_slipsheets     = 2*0.01707 #m^3
        V_tray_broken    = 5.941e-4 #m^3
        V_tray_notbroken = 0.00649 #m^3

        #define quantities
        num_trays     = cases
        num_pallets   = num_trays/2400 
        trashed_trays = num_trays *0.02 # assume 98% efficiency 

        #determine waste volume from tray waste
        #assume 80% of the boxes are broken down, 20% are not broken down 
        V_tray_waste = (num_pallets*V_pallet_covers)+(num_pallets*V_slipsheets)+ ((trashed_trays*0.80)*V_tray_broken)+((trashed_trays*0.20)&V_tray_notbroken)

        return V_tray_waste

    def Cans (self, cases, num_cans):

        #initialize volumes 
        V_can = 4.8657e-4 #m^3

        #define quantities
        trashed_cans = num_cans *0.02

        #determine waste from unsellabe cans 
        V_can_waste = V_can*trashed_cans

        return V_can_waste

    def Plastic_Rolls(self):
        #assume we use 3-4 plastic rolls a day when producing cans (used in tray line)
        #on each pallet of plastic rolls, each row contains 6 rolls and has two thick cardboard sheets aroud it
        
        #initialize volumes 
        V_pallet_sheets = 2*0.1591

        #determine waste from plastic rolls 
        V_plasticroll_waste = V_pallet_sheets

        return V_plasticroll_waste

    def sugar_citric_calc(self, gallons, constant):
        return round((gallons*constant)/50 )

    def sodium_benzonate_calc(self, gallons, constant):
        return round((gallons*constant)/55)

    def Sugar_Citric_NaBenz_Bags(self):
        #from the expected case quantity, we can determine the total gallons of product being produced

        #initialize volume 
        V_sugar      = 0.0029502 #m^3
        V_citric     = 0.0029502 #m^3
        V_sodiumbenz = '' #need to find this value 
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
    



