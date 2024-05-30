#==============================================================================
# Model class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model(Top)

# Temp TODO: 
#   complete sim_step()
#   brainstorm random events and add to event()
#   create data storage variables for values of note that are lost by end of simulation (needs further discussion)
#   create plot system (can wait until the other simulation-related stuff is complete)

#- Imports of packages and modules:
import numpy as N
import random
import matplotlib.pyplot as plt
from building import Building
from poi import PoI
from city import City
from landowner import Landowner
from unit import Unit
from visualize import plot_grid, plot_building_values, plot_landowner_metrics, plot_occupancy_rate

#========================== USER ADJUSTABLE (begin) ==========================
city_size = 50                                                                      # City Size
num_landowners = 20                                                                 # Initial number of Land Owners
num_new_landowners = 10                                                             # Number of Land Owners added during Mid-sim event
num_months = 240                                                                    # Number of months the simulation will run
num_event_interval = 60                                                             # Number of months that pass before a mid-simulation event occurs
num_money_min = 500000.0                                                            # Minimum amount of money a Landowner initializes with
num_money_max = 5000000.0                                                           # Maximum amount of money a Landowner initializes with
num_income_min = 1000.0                                                             # Mininum amount of monthly income a Landowner initializes with
num_income_max = 5000.0                                                             # Maximum amount of monthly income a Landowner initializes with
num_init_buildings_max = 3                                                          # Maximum number of buildings a Landowner initializes with
num_patience_min = 6                                                                # Minimum amount of months a Landowner is willing to wait to start a project
num_patience_max = 24                                                               # Maximum amount of months a Landowner is willing to wait to start a project
owner_type = ["Pass", "Agg", "Mod", "P-Mod", "A-Mod"]                               # Choices of Landowner Disposition/Preference/Type - details in .landowner
num_building_unit_max = 10                                                          # Maximum number of units a building can have
prob_residential = [0.7, 0.8, 0.9, 1.0]                                             # Likeliness of a grid unit being a residential building when initialized
num_poi = 50                                                                        # Initial number of Points of Interest in the City

#=========================== USER ADJUSTABLE (end) ===========================

class Model:
    def __init__(self, prob_res):
        """Model Initialization Function
        
        Initializes City Class, Landowner List, and Simulation Step Count. 
        Initialized Model step-progressed in model.run_sim until intended month is reached.
        """
        self.month = 0                                                              # Initialize Month Count
        self.city = City(city_size, prob_res, num_poi, num_building_unit_max)       # Initialize City using Size, residential probability, and PoI number adjustables
        self.landowners = []                                                        # Initialize Landowner List
        self.retired = []                                                           # Initialize Retired Landowner List
        for _ in range(num_landowners):                                             # Populate Landowner List using:
            money = random.randint(num_money_min, num_money_max)                    # Random int between min and max money adjustable for initial starting funds
            income = random.randint(num_income_min,num_income_max)                  # Random int between min and max income adjustable for monthly income
            patience = random.randint(num_patience_min,num_patience_max)            # Random int between min and max patience adjustable for patience in months
            type = random.choice(owner_type)
            landowner = Landowner(money,income,patience,type)                       # Initialize individual landowner with starting funds, income, and patience
            init_buildings = random.randint(1,num_init_buildings_max)               # Randomize number of buildings landowner will own
            available_buildings = [building for building in self.city.properties if (building.value * 0.2 <= money)] # find available buildings within budget of landowner 
            for _ in range(init_buildings):
                if available_buildings:
                    building = random.choice(available_buildings)
                    landowner.acquire_building(building)
                    available_buildings.remove(building)                            # Ensure the building isn't chosen again

            self.landowners.append(landowner)                                       # Append landowner to list
        self.event_message = "Nothing Yet..."
            

    def run_sim(self, months):
        """Simulation Run Function
        
        Steps model until target month is reached. Triggers random event every 60 months (5 years).
        """
        while (self.month<months):
            self.sim_step()
            if (self.month>0 and self.month%num_event_interval==0): self.event()
        # Visualization at regular intervals or end of simulation
            if self.month % 12 == 0 or self.month == months - 1:
                self.visualize()

    def sim_step(self):
        """Simulation Step Function
        
        Checks step phase of model and updates city/landowners accordingly:
        
        0 - Buildings: Update Tenancies/Vacancies, -> 1
        1 - Landowners: Collect Rent, -> 2
        2 - Buildings: Update Rent based on Owner type -> 3
        3 - Landowners: Pay Upkeep, Update/Begin Decisions/Projects -> 4
        4 - City: Remove Retired Landowners, increment month -> 0

        (The step system is to organize the sequence and more easily insert code to extract data in-between steps.
        Alternatively, we can skip the step system outright and just code the sequence in order)
        """
        #0: Building Occupancy check
        for landowner in self.landowners:
            for building in landowner.buildings:
                prob_tenancy = self.city.get_attractiveness(building)
                for unit in building.units:
                    if not unit.occupied:
                        if random.randint(0,100)<prob_tenancy: unit.fill(building.rent)

        #1: Collect Rent
        for landowner in self.landowners:
            landowner.collect_rent()
            for building in landowner.buildings:
                for unit in building.units:
                    if unit.occupied:unit.step()

        #2: Update/Post Rent
        for landowner in self.landowners:
            for building in landowner.buildings:
                building.post_rent(self.city)

        #3: Upkeep and Decisions
        for landowner in self.landowners:
            landowner.pay_mortgage()
            landowner.pay_upkeep()
            landowner.make_decision(self.city,self.month)


        #4: Remove Landowners, step age
        for landowner in self.landowners:
            if not landowner.buildings:
                self.retired.append(landowner)
                self.landowners.remove(landowner)
        for property in self.city.properties:
            property.age += 1
            property.value *= 1.07177 #assumption: property value doubles every 2 years (at least rent does)
        
        self.month+=1
    
    def event(self,i=random.randint(0,3)):
        """Event Function
        
        Holds an event that occurs in the simulation at random. Function details are held in this function and called by index

        (Events are expected to be random, but for testing purposes or targeted examination may be arbitrarily constant) 
        """
        match i:
            case 0:
                # Pet Damage: Landowners take a fixed hit to their finances for every unit they own with a pet-friendly building
                self.event_message = "Pet Damage: Pet-friendly units lose money"
                for landowner in self.landowners:
                    for building in landowner.buildings:
                        if building.amenities.pets:
                            for unit in building.units:
                                if unit.occupied:
                                    landowner.money -= 5000

            case 1:
                # Crime Zone: An empty plot or unowned residence is replaced by a crime PoI
                self.event_message = "Crime Zone: A Crime spot has appeared"
                self.city.add_poi("Crime")
            case 2:
                # New Blood: More Landowners enter the simulation and get buildings
                self.event_message = "New Blood: %s new landowner(s) entered the simulation"
                for _ in range(num_new_landowners):                                             # Populate Landowner List using:
                    money = random.randint(num_money_min, num_money_max)                    # Random int between min and max money adjustable for initial starting funds
                    income = random.randint(num_income_min,num_income_max)                  # Random int between min and max income adjustable for monthly income
                    patience = random.randint(num_patience_min,num_patience_max)            # Random int between min and max patience adjustable for patience in months
                    type = random.choice(owner_type)
                    landowner = Landowner(money,income,patience,type)                      # Initialize individual landowner with starting funds, income, and patience
                    init_buildings = random.randint(1,num_init_buildings_max)               # Randomize number of buildings landowner will own
                    available_buildings = [building for building in self.city.properties if (building.value * 0.2 <= money)]
                    for _ in range(init_buildings):
                        if available_buildings:
                            building = random.choice(available_buildings)
                            landowner.acquire_building(building)
                            available_buildings.remove(building)                            # Ensure the building isn't chosen again

                    self.landowners.append(landowner)                                       # Append landowner to list
            case 3:
                # Necessary Amenity: Lack of a specific amenity now negatively impacts attractiveness
                more = False
                n_amenity = random.randint(0,7)
                self.event_message = "Necessary Amenity: Prospective tenants desire "
                match n_amenity:
                    case 0: 
                        self.event_message += "pet-friendly units"
                        if self.city.amenity_attract.pets: self.city.amenity_attract.pets=False
                        else: 
                            self.city.amenity_modifier.pets *= 2
                            more = True
                    case 1: 
                        self.event_message += "a parking garage"
                        if self.city.amenity_attract.garage: self.city.amenity_attract.garage=False
                        else: 
                            self.city.amenity_modifier.garage *= 2
                            more = True
                    case 2: 
                        self.event_message += "in-unit laundry"
                        if self.city.amenity_attract.laundry: self.city.amenity_attract.laundry=False
                        else: 
                            self.city.amenity_modifier.laundry *= 2
                            more = True
                    case 3: 
                        self.event_message += "a swimming pool"
                        if self.city.amenity_attract.pool: self.city.amenity_attract.pool=False
                        else: 
                            self.city.amenity_modifier.pool *= 2
                            more = True
                    case 4: 
                        self.event_message += "elevator accessibility"
                        if self.city.amenity_attract.elevator: self.city.amenity_attract.elevator=False
                        else: 
                            self.city.amenity_modifier.elevator *= 2
                            more = True
                    case 5: 
                        self.event_message += "in-unit central heating"
                        if self.city.amenity_attract.heating: self.city.amenity_attract.heating=False
                        else: 
                            self.city.amenity_modifier.heating *= 2
                            more = True
                    case 6: 
                        self.event_message += "in-unit air conditioning"
                        if self.city.amenity_attract.air_conditioner: self.city.amenity_attract.air_conditioner=False
                        else: 
                            self.city.amenity_modifier.air_conditioner *= 2
                            more = True
                    case 7: 
                        self.event_message += "a fitness center"
                        if self.city.amenity_attract.gym: self.city.amenity_attract.gym=False
                        else: 
                            self.city.amenity_modifier.gym *= 2
                            more = True
                
                
                if more: self.event_message += " strongly"


    def visualize(self):
        """Visualization Function
        
        Calls the visualization functions to display the current state of the city and landowners.
        """
        plot_grid(self.city)
        plot_building_values(self.city)
        plot_landowner_metrics(self.landowners)
        plot_occupancy_rate(self.city)
        

# initialize the model
model = Model(prob_residential[0]) # temporarily setting residential probability to 60%, may consider running multiple models of varying probabilities down the road

# run the simulation
model.run_sim(num_months)