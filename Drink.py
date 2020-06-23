from Cans import Can
from Bottles import Bottles

class Drink():
    def __init__(self, name, cases, bottled):
        self.name = name
        self.cases = cases
        self.bottled = bottled
        if bottled:
            self.packaging_waste = Bottles(name, cases)
        else:
            self.packaging_waste = Can(name, cases)