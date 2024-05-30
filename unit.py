#==============================================================================
# Unit class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Unit

# TODO:
#   Describe functions (otherwise, should be done)

import random

class Unit:
    def __init__(self, rent, type=None):
        self.occupied = False
        self.rent = rent
        self.tenancy = 0
        if type==None and bool(random.randint(0,1)):
            self.occupied = True
            self.tenancy = random.randint(1,12)

    def fill(self,rent):
        self.occupied = True
        self.rent = rent
        self.tenancy = random.choice([3,6,12])

    def step(self):
        if self.occupied==True: self.tenancy-=1
        if self.tenancy==0: self.occupied=False
