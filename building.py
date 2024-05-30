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
from unit import Unit
from amenity import Amenities

#========================== USER ADJUSTABLE (begin) ==========================
age_init_max = 60
unit_type_list = ['std','1bd','2bd','3bd']
unit_rent_list = [2000.0,2500.0,3000.0,3500.0]
unit_value_list = [625000.0,1250000.0,2500000.0,5000000.0]

#=========================== USER ADJUSTABLE (end) ===========================

class Building(object):
    def __init__(self, x, y, unit_max, type=None, owner=None, age=None, amenities=None):
        """Building Initialization Function
        
        Initializes building to given parameters or random values if not provided (None)"""
        self.location = (x, y)
        self.type = type
        if (self.type==None): self.type = random.choice(unit_type_list)
        self.rent = unit_rent_list[unit_type_list.index(self.type)]
        self.owner = owner
        self.age = age
        if (self.age==None): self.age=random.randint(0,age_init_max)
        self.amenities = amenities
        if (self.amenities==None): self.amenities = Amenities('rand')
        self.init_units(random.randint(1,unit_max))
        self.value = unit_value_list[unit_type_list.index(self.type)]

    def init_units(self, num_units):
        """Units Initialization Function, used as part of building.__init__()
        
        Sets number of units in the building and populates unit list with randomly generated units that may or may not be occupied"""
        self.num_units = num_units
        self.units = []
        for _ in range(num_units): self.units.append(Unit(self.rent)) # TODO change rent 

    def add_unit(self):
        """Add Unit Function, used during building improvement option of model.sim_step()
        
        Adds one new unit to unit list"""
        self.units.append(Unit('NEW'))
        self.update_upkeep()
        self.update_value()

    def post_rent(self):
        """Post New Rent Function, used during Rent Update at model.sim_step()
        
        Updates building's posted rent in accordance to landowner's type and market average"""
        

    def update_rental_income(self):
        """Rental Income Update Function, used before each Rent Collection at model.sim_step()
        
        Sets building's rental income value to total rent of currently occupied units"""
        self.rental_income = 0
        for unit in self.units:
            if unit.occupied==True:
                self.rental_income += unit.rent

    def update_upkeep(self,amenity_upkeep):
        """Upkeep Update Function, used before each Pay Upkeep at model.sim_step()
        
        Sets building's upkeep to # of units * (per-unit upkeep + per-unit amenity upkeep)"""
        per_unit_amenity_upkeep = 0
        # placeholder for "if building has a certain amenity, add global upkeep for that amenity to per_unit_amenity_upkeep"
        self.upkeep = self.num_units*(self.unit_upkeep+per_unit_amenity_upkeep)
        
        
    def add_amenity(self, type):
        """Add Amenity Function, used during Decision at model.sim_step()
        
        Adds specific amenity to building's amenities class, changing its respective value from False to True (see .amenity)"""
        # placeholder for "change respective amenities.**** value to True"

    def renovate(self):
        """Renovate Function, used during Decision at model.sim_step()
        
        Resets building age to 0 (that's it)"""
        self.age = 0

    def update_value(self, attractions, cost):
        """Update Building Value function, used before selling property in Decision at model.sim_step() 
        
        Sets building's value to fixed base value + amenity costs (global) for each amenity present + Unit Value for each unit"""
        # Calculate the value based on proximity to attractions, age, units, and amenities
        base_value = 100  # Base value for every building
        # attraction_bonus = 50 * self.proximity_to_attractions
        age_penalty = max(0, 50 - self.age)  # Value decreases as building gets older
        amenities_bonus = 20 * len(self.amenities)
        units_value = 30 * len(self.units)
        self.value = base_value + age_penalty + amenities_bonus + units_value
    
