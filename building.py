#==============================================================================
# Building class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building

#- Imports of packages and modules:
import numpy as N
from .unit import Unit

#========================== USER ADJUSTABLE (begin) ==========================
unit_types = ["std", "1x1", "2x1", "2x2", "3x2", "3x3"]

#=========================== USER ADJUSTABLE (end) ===========================

class Building(object):
    def __init__(self, x, y):
        self.location = (x, y)
        self.owner = None
        self.status = 'uninhabited'  # or 'inhabited' or 'available for rent'
        self.age = 0
        self.amenities = []
        self.units = []
        self.proximity_to_attractions = 0
        self.value = 0  # increase based on attractions, when renovated, and when amenities are added 

    def add_unit(self, unit):
        self.units.append(unit)
        self.update_value()
        
    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        self.update_value()

    def renovate(self):
        self.age = 0
        self.update_value()

    def update_value(self):
        # Calculate the value based on proximity to attractions, age, units, and amenities
        base_value = 100  # Base value for every building
        attraction_bonus = 50 * self.proximity_to_attractions
        age_penalty = max(0, 50 - self.age)  # Value decreases as building gets older
        amenities_bonus = 20 * len(self.amenities)
        units_value = 30 * len(self.units)
        self.value = base_value + attraction_bonus + age_penalty + amenities_bonus + units_value
    
