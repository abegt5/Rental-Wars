#==============================================================================
# Point of Interest class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->PoI

#- Imports of packages and modules:
import random

class PoI:
    def __init__(self, x, y, poi_type=None):
        self.location = (x, y)
        self.type = poi_type
        self.influence = 0
        if self.type==None: self.type = random.choice(["Small", "Medium", "Large"])
        if self.type == "Small":
            self.influence = 10
        elif self.type == "Medium":
            self.influence = 15
        elif self.type == "Large":
            self.influence = 20
        elif self.type == "Crime":
            self.influence = 20
       
    def distance_to(self, building):
        """Calculate the distance from the PoI to a given building."""
        return ((self.location[0] - building.location[0]) ** 2 + (self.location[1] - building.location[1]) ** 2) ** 0.5

    def influence_attractiveness(self, building):
        """Influence the attractiveness of a building based on the type of PoI and distance."""
        distance = self.distance_to(building)
        if distance <= self.influence:
            if self.type in ["Small", "Medium", "Large"]:
                return 1  # Positive influence
            elif self.type == "Crime":
                return -1  # Negative influence
        return 0  # No influence


