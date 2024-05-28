#==============================================================================
# Amenity class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Amenity

class Amenity:
    def __init__(self, type, cost):
        self.type = type
        self.cost = cost
