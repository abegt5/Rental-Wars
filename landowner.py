#==============================================================================
# Landowner class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->Landowner(List)->Landowner(Individual)

#- Imports of packages and modules:
import random
import numpy as N

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
    def __init__(self, money, income, patience, preference):
        """Landowner Initialization Function
        
        Initializes money and patience to argument passed via model.__init__"""
        self.money = money  # Initial funds
        self.income = income  # Monthly income
        self.patience = patience  # Months willing to wait for a project
        self.preference = preference
        if (self.preference==None): self.preference = random.choice(type_list)
        self.buildings = []  # List of buildings owned
        self.mortgages = {}  # Dictionary to track mortgage payments {building: monthly_payment}
        self.decisions = []

    def acquire_building(self, building):
        """Building Acquisition Function, used during Land Acquisition option of model.sim_step()
        
        Assigns specified unowned building in city to landowner"""
        mortgage_rate=0.05
        mortgage_term=360
        down_payment = building.value * 0.2  # Example down payment: 20% of the building value
        if self.money >= down_payment:
            self.money -= down_payment
            self.buildings.append(building)
            building.owner = self
            # Calculate mortgage
            loan_amount = building.value - down_payment
            monthly_payment = self.calculate_monthly_mortgage_payment(loan_amount, mortgage_rate, mortgage_term)
            self.mortgages[building] = monthly_payment

    def calculate_monthly_mortgage_payment(self, loan_amount, rate, term):
        """Calculates the monthly mortgage payment using the loan amount, interest rate, and term."""
        monthly_rate = rate / 12
        return loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -term) # the annuity formula

    def sell_building(self, building):
        """Sells a building, updates the landowner's money, and removes the mortgage."""
        if building in self.buildings:
            self.buildings.remove(building)
            self.money += building.value  # Assuming building value is equal to the selling price
            building.owner = None
            del self.mortgages[building]

    def redevelop_building(self, building):
        """Redevelops a building, resetting its age and potentially adding value."""
        if building in self.buildings:
            building.renovate()
            self.money -= building.value * 0.1  # Cost of redevelopment (example: 10% of building value)

    def collect_rent(self):
        """Collects rent from all owned buildings."""
        for building in self.buildings:
            self.money += sum(unit.rent for unit in building.units if unit.occupied)

    def pay_upkeep(self):
        """Pays upkeep costs for all owned buildings"""
        
        self.money -= sum(building.upkeep for building in self.buildings)

    def pay_mortgage(self):
        """Pays mortgage costs for all owned buildings."""
        total_mortgage_payment = sum(self.mortgages.values())
        self.money -= total_mortgage_payment

    def make_decision(self, city, month):
        """Decides whether to acquire, sell, or redevelop buildings based on the landowner's preference."""
        decision = {}  # Create a dictionary to store the decision
        decision['month'] = month  # Record the month when the decision is made
        decision['action'] = 'None'

        if self.preference == "Agg" and self.money > 50000:  # Aggressive: Acquire new buildings aggressively
            for property in city.properties:
                if property.owner is None:
                    self.acquire_building(property)
                    decision['action'] = 'Acquire'
                    break       
        elif self.preference == "Pass" :  # Passive: Do nothing 
            decision['action'] = 'Pass'
            pass
        elif self.preference == "Mod":  # Moderate: Improve existing buildings
            for building in self.buildings:
                if building.age > 15:
                    self.redevelop_building(building)
                    decision['action'] = 'Improve'
                    break
        elif self.preference == "P-Mod" and self.patience >= 12:  # Passive-Moderate: Sometimes redevelop buildings
            for building in self.buildings:
                if building.age > 20 and random.random() < 0.5:
                    self.redevelop_building(building)
                    decision['action'] = 'Improve'
                    break
        elif self.preference == "A-Mod" and self.money > 100000:  # Aggressive-Moderate: Acquire or improve buildings
            for building in self.buildings:
                if building.age > 10:
                    self.redevelop_building(building)
                    decision['action'] = 'Improve'
                    break
            for property in city.properties:
                if property.owner is None:
                    self.acquire_building(property)
                    decision['action'] = 'Acquire'
                    break       
        self.decisions.append(decision)
       