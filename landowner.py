#==============================================================================
# Landowner class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->Landowner(List)->Landowner(Individual)

# TODO:
#   complete assign_building()
#   complete acquire_building()
#   complete update_upkeep()
#   complete update_rental_income()

#- Imports of packages and modules:
import random

#========================== USER ADJUSTABLE (begin) ==========================
type_list = ["Pass", "Agg", "Mod", "P-Mod", "A-Mod"]

#=========================== USER ADJUSTABLE (end) ===========================
# Basic Explanation of Landowner Types
# "Passive" - Does nothing
# "Aggressive" - Spends recklessly, prioritizes acquiring new buildings
# "Moderate" - Spends conservatively, preserves existing funds and prefers improving buildings over acquiring new ones
# "Passive-Moderate" - Moderate behavior, but sometimes does nothing
# "Aggressive-Moderate" - Shared priority in building acquisition and improvement

# Note: actual decision making, probabilities, and money increases/deductions occur in model, not here

class Landowner:
    def __init__(self, money, income, patience, type=None):
        """Landowner Initialization Function
        
        Initializes money and patience to argument passed via model.__init__"""
        self.money = money # net worth, rent - morgage + building value - expenses
        self.nonrent_income = income
        self.buildings = []
        self.patience = patience
        self.type = type
        if (self.type==None): self.type = random.choice(type_list)
        self.update_rental_income()
        self.update_upkeep()

    def assign_building(self,city):
        """Building Assignment Function, used during model initialization
        
        Randomly assigns unowned building in city to landowner"""

    def acquire_building(self, city):
        """Building Acquisition Function, used during Land Acquisition option of model.sim_step()
        
        Assigns specified unowned building in city to landowner"""

    def update_upkeep(self):
        """Update Upkeep Function, called during landowner initialization and whenever landowner's property details change regarding upkeep
        
        Reassigns upkeep value to combined values of individual property upkeep"""

    def update_rental_income(self):
        """Update Rental Income Function, used during landowner initialization and whenever landowner's property details change regarding unit occupancy
        
        Reassigns rental income value to combined values of individual property rental income"""


