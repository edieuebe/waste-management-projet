import Cans
import Bottles

class Drink():
    __init__(self, name, cases, bottled):
        self.name = name
        self.cases = cases
        self.bottled = bottled
        if bottled:
            self.packaging_waste = Bottles(name, cases)
        else:
            self.packaging_waste = Cans(name, cases)