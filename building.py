#==============================================================================
# Building class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building

# TODO:
#   Stuff (I'm too tired to process what)

#- Imports of packages and modules:
import random
from .unit import Unit

#========================== USER ADJUSTABLE (begin) ==========================
units_min = 1
units_max = 8
age_max = 60
status_list = ['EMPTY', 'RENTING', 'OCCUPIED']

#=========================== USER ADJUSTABLE (end) ===========================

class Building(object):
    def __init__(self, x, y, owner=None, age=None, amenities=None, units=None):
        """Building Initialization Function
        
        Initializes building to given parameters or random values if not provided (None)"""
        self.location = (x, y)
        self.owner = owner
        self.status = 'EMPTY'
        self.age = age
        if (self.age==None): self.age=random.randint(0,age_max)
        self.amenities = amenities
        if (self.amenities==None): self.amenities = []
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
    
