#==============================================================================
# Model class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================

#- Imports of packages and modules:
import numpy as N
import matplotlib.pyplot as plt
from .Attraction import Attraction
from .building import Building
from city import City
from .landowner import Landowner
from .unit import Unit
from .driver import Driver
from . import visualize as V

class Model:
    def __init__(self, city_size=50, num_landowners=50):
        self.city = City(city_size)
        self.landowners = []
        self.init_landowners(num_landowners)
    
    def init_landowners(self, num_landowners):
        for _ in range(num_landowners):
            money = random.randint(5000, 200000)  # example range
            preference = random.choice([])
            patience = random.randint(1, 10)
            self.landowners.append(Landowner(money, preference, patience))

    def add_building_to_city(self, building):
        self.city.add_building(building)

    def add_attraction_to_city(self, attraction):
        self.city.add_attraction(attraction)

    def run_simulation(self, steps):
        for _ in range(steps):
            self.simulation_step()

    def simulation_step(self):
        # update building ages and statuses
        for row in self.city.grid:
            for building in row:
                if building:
                    building.age += 1
                    # additional logic for updating status, collecting rent, etc

        # Landowner actions
        for landowner in self.landowners:
            # example of a decison a landowner can make change or add more 
            if landowner.money > 50000:
                for x in range(self.city.size):
                    for y in range(self.city.size):
                        building = self.city.get_building(x, y)
                        if building and building.owner is None:
                            landowner.acquire_building(building)

# example usage
import random

# initialize the model
model = Model(city_size=50, num_landowners=50)

# add some attractions
model.add_attraction_to_city(Attraction(x=10, y=10, type='school', value_increase_radius=5))
model.add_attraction_to_city(Attraction(x=20, y=20, type='mall', value_increase_radius=8))

# add some buildings
building1 = Building(x=5, y=5)
building1.add_unit(Unit(rent_amount=1000, tenancy_period=12))
model.add_building_to_city(building1)

building2 = Building(x=15, y=15)
building2.add_unit(Unit(rent_amount=1200, tenancy_period=12))
model.add_building_to_city(building2)

# run the simulation
model.run_simulation(steps=12)  # Simulate 12 time steps for months or year need to decide depnding on questions being answered