#==============================================================================
# Visualization functions for the Model
# Used in CSS 458 A Spring 2024 Final Project - Rental Wars
#
# Team Digital Directors
# May 2024
#==============================================================================

#- Imports of packages and modules:
import numpy as N
import matplotlib.pyplot as plt
from poi import PoI
from building import Building

def plot_grid(city, mode=None, month=None):
    """Plot the city grid with buildings and points of interest."""
    size = city.size
    grid = city.grid
    fig, ax = plt.subplots(figsize=(10, 10))

    # Create a colormap for different types of buildings and POIs
    cmap = plt.get_cmap("tab20")
    colors = {
        "Small": cmap(1),
        "Medium": cmap(2),
        "Large": cmap(3),
        "Crime": cmap(6),
        "Residential": cmap(5),
        "Unowned": cmap(10)
    }

    for x in range(size):
        for y in range(size):
            if isinstance(grid[x][y], PoI):
                poi = grid[x][y]
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=colors[poi.type], label=poi.type))
            elif isinstance(grid[x][y], Building) and grid[x][y].owner!=None:
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=colors["Residential"], label="Residential"))
            elif isinstance(grid[x][y], Building) and grid[x][y].owner==None:
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=colors["Unowned"], label="Unowned"))

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_xticks(N.arange(0, size+1, 1))
    ax.set_yticks(N.arange(0, size+1, 1))
    ax.grid(which='both')
    ax.set_aspect('equal')
    if mode=="anim":plt.title('City Grid - Month #%s' % month)
    else : plt.title('City Grid - End of Sim')
    plt.legend(handles=[plt.Line2D([0], [0], color=colors[key], lw=4) for key in colors],
               labels=[key for key in colors])
    if mode=="anim": plt.pause(2)

def plot_building_values(city):
    """Plot the values of the buildings in the city grid."""
    size = city.size
    grid = city.grid
    building_values = N.zeros((size, size))

    for x in range(size):
        for y in range(size):
            if isinstance(grid[x][y], Building):
                building_values[x][y] = grid[x][y].value

    plt.figure(figsize=(10, 10))
    plt.imshow(building_values, cmap="viridis", origin="lower")
    plt.colorbar(label='Building Value')
    plt.title('Building Values in the City Grid - End of Sim')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

def plot_landowner_metrics(landowners):
    """Plot the net worth and decisions of landowners."""
    net_worths = [landowner.money for landowner in landowners]
    decisions = [landowner.decisions for landowner in landowners]

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color = 'tab:blue'
    ax1.set_xlabel('Landowners')
    ax1.set_ylabel('Net Worth', color=color)
    ax1.plot(range(len(landowners)), net_worths, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:green'
    ax2.set_ylabel('Decisions', color=color)

    # Define markers and colors for different actions
    action_markers = {'Acquire': 'o', 'Pass': 's', 'Improve': '^', 'None': 'x'}
    action_colors = {'Acquire': 'tab:orange', 'Pass': 'tab:purple', 'Improve': 'tab:red', 'None': 'tab:gray'}
    
    # Create a set to keep track of added labels for the legend
    handles = []
    labels = []
    
    # Plot decisions for each landowner
    for idx, decision_list in enumerate(decisions):
        for decision in decision_list:
            action = decision['action']
            month = decision['month']
            sc = ax2.scatter(month, idx, marker=action_markers[action], color=action_colors[action], label=action, alpha=0.7)
            if action not in labels:
                handles.append(sc)
                labels.append(action)
    
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_yticks(range(len(landowners)))
    ax2.set_yticklabels([f'Landowner {i+1}' for i in range(len(landowners))])

    # Create a legend using the handles and labels collected
    ax2.legend(handles, labels, loc='upper left')

    plt.title('Net Worth and Decisions of Landowners - End of Sim')

def plot_occupancy_rate(city):
    """Plot the occupancy rate of buildings in the city grid."""
    size = city.size
    grid = city.grid
    occupancy_rates = N.zeros((size, size))

    for x in range(size):
        for y in range(size):
            if isinstance(grid[x][y], Building):
                building = grid[x][y]
                occupied_units = sum(unit.occupied for unit in building.units)
                total_units = len(building.units)
                occupancy_rates[x][y] = occupied_units / total_units if total_units > 0 else 0

    plt.figure(figsize=(10, 10))
    plt.imshow(occupancy_rates, cmap="coolwarm", origin="lower")
    plt.colorbar(label='Occupancy Rate')
    plt.title('Occupancy Rates in the City Grid - End of Sim')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')

def plot_landowner_finances(data):
    plt.figure(figsize=(10, 10))
    plt.title('Average Landowner Finances over simulation period')
    plt.xlabel('Months')
    plt.ylabel('Finances')
    x = [d[0] for d in data]
    y1 = [d[1] for d in data]
    y2 = [d[2] for d in data]
    y3 = [d[3] for d in data]
    y4 = [d[4] for d in data]
    y5 = [d[5] for d in data]
    plt.plot(x,y1,label='Aggressive Landowners')
    plt.plot(x,y2,label='Passive Landowners')
    plt.plot(x,y3,label='Moderate Landowners')
    plt.plot(x,y4,label='Aggressive-Moderate Landowners')
    plt.plot(x,y5,label='Passive-Moderate Landowners')
    plt.show()

#show value of buildings 
#show increase and decrease of net worth of landowners
#show percent growth and decisons they have made
