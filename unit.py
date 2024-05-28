#==============================================================================
# Unit class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Unit

class Unit:
    def __init__(self, rent_amount, tenancy_period):
        self.occupied = False
        self.tenancy_period = tenancy_period
        self.rent_amount = rent_amount
