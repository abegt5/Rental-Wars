#==============================================================================
# Landowner class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->Landowner(List)->Landowner(Individual)

#- Imports of packages and modules:
import numpy as N

class Landowner:
    def __init__(self, money, preference, patience):
        self.money = money # net worth, rent - morgage + building value - expenses
        self.buildings = []
        self.preference = preference
        self.patience = patience

    def acquire_building(self, building):
        if self.money >= building.value:
            self.money -= building.value
            self.buildings.append(building)
            building.owner = self

    def redevelop_building(self, building):
        # implementation for redevelopment
        # call renovate for buildings
        return None


