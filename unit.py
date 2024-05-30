#==============================================================================
# Unit class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Unit

#- Imports of packages and modules:
import random

class Unit:
    def __init__(self, rent, init=None):
        """Unit Initialization Function
        
        Initializes Unit with occupancy status, rent number, and tenancy length. 
        When initialized as part of building initialization, randomizes occupancy and tenancy length. 
        Otherwise, always initializes empty (because unit is newly added to building). """
        self.occupied = False
        self.rent = rent
        self.tenancy = 0
        if init==None and bool(random.randint(0,1)):
            self.occupied = True
            self.tenancy = random.randint(1,12)

    def fill(self,rent):
        """Unit Occupation Function
        
        Fills unit with tenant, changing its occupancy status.
        Updates rent to provided rent value, randomizes tenancy to 3/6/12-month lease"""
        self.occupied = True
        self.rent = rent
        self.tenancy = random.choice([3,6,12])

    def step(self):
        """Unit-specific Time-step Function
        
        Passes a month in terms of unit occupancy.
        If Tenancy expires, unit is no longer vacant"""
        if self.occupied==True: self.tenancy-=1
        if self.tenancy==0: self.occupied=False
