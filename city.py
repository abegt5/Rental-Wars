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
        self.size = size
        self.amenity_attract = Amenities('All')
        self.amenity_modifier = Amenities('Num')
        self.amenity_modifier.change_values([random.randint(1,5) for _ in range(8)])
        self.amenity_cost = Amenities('Num')
        self.amenity_cost.change_values([0.0,20000.0,1000.0,10000.0,10000.0, 5000.0, 5000.0, 10000.0])
        self.amenity_upkeep = Amenities('Num')    
        self.amenity_upkeep.change_values([0.0,100.0,200.0,150.0,200.0,200.0,200.0,100.0])
        for _ in range(num_poi): self.add_poi()
        self.add_init_buildings(prob_res,num_building_unit_max)

    def add_poi(self, type=None):
        """Add Points of Interest Function"""
        miss = True
        while miss:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y] is None:
                miss = False
                poi = PoI(x, y, type)
                self.pois.append(poi)
                self.grid[x][y] = poi
        
    def add_init_buildings(self,prob_res,num_building_unit_max):
        """Add Residences (initial) Function
        
        Navigates the entire city grid, checks to make sure the grid unit is empty(None) and generates a new building at a set probability.
        New residential building is allocated to respective grid space and appended to Property List
        Initially generated buildings are randomized in unit type, unit limit, age, and amenities"""
        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] is None:
                    if random.random() < prob_res:
                        unit_max = random.randint(1, num_building_unit_max)
                        building = Building(x, y, unit_max, self.amenity_upkeep)
                        self.grid[x][y] = building
                        self.properties.append(building)

    def add_building(self,building):
        
        """Add Building (mid-simulation) Function, to be used during 'new competition' event or landowner acquisition of undeveloped land
        
        Checks city grid to ensure location is empty(None), then generates a new building at coordinates and appends it to Property List.
        New building will likely have arbitrarily established values for unit type, limit, and amenities. Age will be fixed at 0"""
        x, y = building.location
        self.grid[x][y] = building
        self.properties.append(building)

    def get_nearby_buildings(self, building, radius):
        """Get all buildings within a given radius of the specified building."""
        nearby_buildings = []
        for i in range(max(0, building.location[0] - radius), min(self.size, building.location[0] + radius + 1)):
            for j in range(max(0, building.location[1] - radius), min(self.size, building.location[1] + radius + 1)):
                if type(self.grid[i][j])== Building and self.grid[i][j] != building:
                    nearby_buildings.append(self.grid[i][j])
        return nearby_buildings

    def get_average_rent_nearby(self, building, radius):
        """Calculate the average rent of buildings within a given radius."""
        nearby_buildings = self.get_nearby_buildings(building, radius)
        if not nearby_buildings:
            return 0
        return sum(b.rent for b in nearby_buildings) / len(nearby_buildings)

    def get_attractiveness(self, building):
        """Calculate the attractiveness of a building based on various factors."""
        base_attractiveness = 50  # Starting base attractiveness percentage
        amenity_bonus = sum(value * 5 for value in building.amenities.list() if isinstance(value, bool) and value)
        poi_modifier = sum(poi.influence_attractiveness(building) for poi in self.pois)
        average_rent = self.get_average_rent_nearby(building, 5)  # Using a fixed radius of 5 for rent comparison
        rent_deviation = (average_rent - building.rent) / average_rent if average_rent != 0 else 0
        rent_modifier = max(0, min(20, 20 * rent_deviation))  # Cap rent modifier between 0 and 20%
        age_modifier = max(0, min(20, building.age // 5))  # Assuming age modifier of 4% reduction per 5 years, capped at 20%

        attractiveness = (base_attractiveness + amenity_bonus + poi_modifier + rent_modifier - age_modifier)
        return max(0, min(100, attractiveness))  # Ensure attractiveness is between 0 and 100

    def get_building(self, x, y):
        return self.grid[x][y]
    
    # Jeremy: Don't know when this gets used
    # update the proximity_to_attractions attribute for all buildings based on their distance to each attraction
    def update_buildings_proximity_to_attractions(self):
        for attraction in self.attractions:
            for x in range(self.size):
                for y in range(self.size):
                    building = self.grid[x][y]
                    if building:
                        distance = abs(attraction.location[0] - x) + abs(attraction.location[1] - y)
                        if distance <= attraction.value_increase_radius:
                            building.proximity_to_attractions += 1  # or any specific value logic
                            building.update_value()
