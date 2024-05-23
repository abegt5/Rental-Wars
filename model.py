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
from .building import Building
from .landowner import Landowner
from .driver import Driver
from . import visualize as V

#========================== USER ADJUSTABLE (begin) ==========================
# Plot Dimensions
grid_x = 25
grid_y = 25

#=========================== USER ADJUSTABLE (end) ===========================

class Model():
    """
    
    """
    def __init__(self):
        self.num_owners = 0
        self.num_retired = 0
        self.mean_finances = 0.0
        self.grid = [[Building() for i in range(grid_y)] for j in range(grid_x)]
        self.list_owners = []
        self.list_retired = []
        self.driver = Driver()
        
    def init_landowners():
        return

    def step():
        return
