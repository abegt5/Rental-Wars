#==============================================================================
# Amenities class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Amenities

#- Imports of packages and modules:
import random

class Amenities:
    def __init__(self, init):
        """Amenities Class Initialization Function
        
        Initializes individual values for each Amenity possible as a pseudo-list
        -When initialized by a building (building.amenity) or as the city's amenity attractiveness indicator (city.amenity_attract), values are boolean
        --building.amenity indicates whether or not the building has those particular amenities
        --city.amenity_attract indicates whether presence of amenity increases attractiveness (true) or absence reduces attractiveness (false)
        -When initialized as the city's attractiveness modifier (city.amenity_modifier), production cost (city.amenity_cost), or upkeep cost (city.amenity_upkeep), values are float
        --city.amenity_modifier indicates amount of attractiveness (in occupation probability) affected
        --city.amenity_cost indicates how much money is required to build the amenity per unit
        --city.amenity_upkeep indicates how much monthly upkeep (also in money) the amenity requires per unit"""

        if init=='All': fill_list = [True for _ in range(8)]
        elif init=='Rand': fill_list = [bool(random.randint(0,1)) for _ in range(8)]
        elif init=='Num': fill_list = [0.0 for _ in range(8)]
        else: fill_list = [None for _ in range(8)]
        
        self.pets = fill_list[0]
        self.garage = fill_list[1]
        self.laundry = fill_list[2]
        self.pool = fill_list[3]
        self.elevator = fill_list[4]
        self.heating = fill_list[5]
        self.air_conditioner = fill_list[6]
        self.gym = fill_list[7]

    def change_values(self,value_list):
        """Multiple Values Assignment Function, used to modify multiple elements of the Amenities class
        
        Allocates list values to respective Amenity in class"""
        self.pets = value_list[0]
        self.garage = value_list[1]
        self.laundry = value_list[2]
        self.pool = value_list[3]
        self.elevator = value_list[4]
        self.heating = value_list[5]
        self.air_conditioner = value_list[6]
        self.gym = value_list[7]

    def list(self):
        """List Function, used when extracting values from two separate Amenity classes
        
        Returns a list of Amenity values"""
        return [self.pets,self.garage,self.laundry,self.pool,self.elevator,self.heating,self.air_conditioner,self.gym]
