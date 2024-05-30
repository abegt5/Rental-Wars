#==============================================================================
# Amenities class
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================
# Class Hierarchy: Model->City->Building->Amenities

# TODO:
#   Expand/Finalize Amenities List
#   Create Initialization Presets for Amenities List

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

        # placeholders for amenities list, values are modified during initialization based on string given in "init" parameter/argument
        self.pets = None
        self.garage = None
        self.laundry = None
        self.pool = None
        self.elevator = None
        self.air_conditioner = None
        self.gym = None


