#==============================================================================
# Point of Interest class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->PoI

class PoI:
    def __init__(self, x, y, type, value_increase_radius):
        self.location = (x, y)
        self.type = type
        self.value_increase_radius = value_increase_radius
