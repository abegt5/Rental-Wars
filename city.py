#==============================================================================
# City class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City

# TODO:
#   Complete add_attractions()
#   Complete add_init_buildings()
#   Define and finalize attractiveness (as a probability)
#   Add functions for random events called in model.event()
#   Set values for amenity modifier, cost, and upkeep

#- Imports of packages and modules:
import numpy as N
import random
from building import Building
from poi import PoI
from amenity import Amenities

class City(object):
    def __init__(self, size, prob_res, num_poi, num_building_unit_max):
        """City Initialization Function

        Initializes City Grid, Property List, Attraction List, and Bad Spots List"""
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.properties = []
        self.pois = []
        self.bad_spots = []
        self.size = size
        self.amenity_attract = Amenities('All')
        self.amenity_modifier = Amenities('Num')
        self.amenity_modifier.change_values([(((random.random()*4)+1)/100) for _ in range(8)])
        self.amenity_cost = Amenities('Num')
        self.amenity_cost.change_values([])
        self.amenity_upkeep = Amenities('Num')
        self.add_attractions(num_poi)
        self.add_init_buildings(prob_res,num_building_unit_max)

    def add_attractions(self, num_poi):
        """Add Points of Interest Function
        
        Randomly generates a pair of coordinates on the city grid to add attractions.
        If coordinate is empty(None), generates a new attraction (of random type), attaches it to the grid, and appends it to the attraction list
        If an attraction already exists at given coordinate pair, generates a new pair
        
        For simplicity's sake, attractions are constant do not change throughout the simulation
        
        Warning: PoI class will contain Bad Spots as a type, which should only be used during events and not initialization. Adjust random accordingly."""
        
    def add_init_buildings(self,prob_res,num_building_unit_max):
        """Add Residences (initial) Function
        
        Navigates the entire city grid, checks to make sure the grid unit is empty(None) and generates a new building at a set probability.
        New residential building is allocated to respective grid space and appended to Property List
        Initially generated buildings are randomized in unit type, unit limit, age, and amenities"""

    def add_building(self,building):
        """Add Building (mid-simulation) Function, to be used during 'new competition' event or landowner acquisition of undeveloped land
        
        Checks city grid to ensure location is empty(None), then generates a new building at coordinates and appends it to Property List.
        New building will likely have arbitrarily established values for unit type, limit, and amenities. Age will be fixed at 0"""
        x, y = building.location
        self.grid[x][y] = building

    # Might belong in model.sim_step() instead of here
    def get_attractiveness(self, building):
        """Get Attractiveness Function, used in model.sim_step() at step 0 to update individual building vacancies"""
        attractiveness = 0
        for PoI in self.pois:
            attractiveness += PoI.influence_attractiveness(building)
        
        """Returns value based on nearby attractions, bad spots, amenities, and rent deviation from average of nearby units (specifics TBD)""" 

    # Jeremy: Don't know when this gets used
    def get_building(self, x, y):
        return self.grid[x][y]
    
