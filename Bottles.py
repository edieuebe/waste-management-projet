class Bottles():
    def __init__(self, name, cases):
        self.name=name #should be specific to drink
        self.cases=cases #Number of cases to be produced
        self.isInProduction= True
        self.num_bottles = cases*6 #6 bottles per case

    def bottles(self, cases, num_bottles):
        # each pallet of empty bottles contains 1,144 bottles
        # there are 8 rows, 143 bottles per row
        # for each row, there is a large four sided, no lid, cardboard box with a divider inside seperating each bottle from each other
        #there is a large cardboard slip sheet on the bottom of each pallet

        #initialize volumes 
        V_bottle = 0.00612 #m^3
        V_box_divider_CB = 0.0621 #m^3
        V_slipsheet = 0.003934 #m^3

        #initialize quantities 
        num_pallets = num_bottles/1144 #number of pallets used=number of slipsheets thrown away 
        num_rows = num_bottles/143 #if there are 143 bottles per row, dividing the total num of bottles by 143 should give num of rows
        trashed_bottles = num_bottles*0.02

        #determine waste volume from bottle packaging
        V_bottle_waste = (num_pallets*V_slipsheet)+(V_bottle*trashed_bottles)+(num_rows*V_box_divider_CB)

        return V_bottle_waste

    def Cartons(self, cases):
        # in each carton, there are 6 bottles
        # inside each carton, there is a CB divider that seperates the bottles
        # the dividers come in a large CB box: 200 dividers per box 
        # cartons come in bundles of 22 with a plastic ziptie holding it together 
        # each pallet holds 24 bundles of cartons with one slipsheet per bundle with 3 large cardboard pieces holding it together on the top

        #initialize volumes 
        V_carton = 0.00217 #m^3
        V_slipsheet = 0.003934 #m^3
        V_dividerbox = 0.00524 #m^3 assume broken down, 
        # assume the dividers themselves do not become waste since they are hand-installed, the waste is minimal

        # initialize quantities
        num_bundles = cases/22 
        num_pallets = cases/528 #total of 528 cartons per pallet if 24 bundles *22 = 528
        num_divider_box = cases/200 
        trashed_cartons = cases*0.01 #assume 99% efficiency

        #determine waste volume from carton packaging and waste
        V_carton_waste = (num_pallets*V_slipsheet)+(num_divider_box*V_dividerbox)+(trashed_cartons*V_carton)

        return V_carton_waste

    def Corks(self, cases):
        # there are 1800 corks per box 

        #initialize volumes 
        V_box = 0.00519 #m^3
        V_cork = 9.7752e-5 #m^3

        # initialize quantities
        num_box = (cases*6)/200 
        trashed_corks = (Cases*6)*0.01 # assume 99% efficiency 

        # determine waste volume from cork pacakging 
        V_cork_waste = (num_box*V_box)+(trashed_corks*V_cork)
   
