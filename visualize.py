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

def plot_grid(city):
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
        "Crime": cmap(4),
        "Residential": cmap(5)
    }

    for x in range(size):
        for y in range(size):
            if isinstance(grid[x][y], PoI):
                poi = grid[x][y]
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=colors[poi.type], label=poi.type))
            elif isinstance(grid[x][y], Building):
                ax.add_patch(plt.Rectangle((x, y), 1, 1, color=colors["Residential"], label="Residential"))

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_xticks(N.arange(0, size+1, 1))
    ax.set_yticks(N.arange(0, size+1, 1))
    ax.grid(which='both')
    ax.set_aspect('equal')
    plt.title('City Grid')
    plt.legend(handles=[plt.Line2D([0], [0], color=colors[key], lw=4) for key in colors],
               labels=[key for key in colors])
    plt.show()

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
    plt.title('Building Values in the City Grid')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

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

    # Flatten the decisions list to extract 'action' for each landowner
    action_labels = {'Acquire': 1, 'Pass': 2, 'Improve': 3, 'None': 4}
    for idx, decision_list in enumerate(decisions):
        actions = [action_labels[decision['action']] for decision in decision_list]
        months = [decision['month'] for decision in decision_list]
        ax2.plot(months, [idx] * len(actions), 'o', label=f'Landowner {idx+1}', alpha=0.7)  # Plot each decision as a point

    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_yticks(range(len(landowners)))
    ax2.set_yticklabels([f'Landowner {i+1}' for i in range(len(landowners))])

    plt.title('Net Worth and Decisions of Landowners')
    plt.legend(loc='upper left')
    plt.show()



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
    plt.title('Occupancy Rates in the City Grid')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()


#show value of buildings 
#show increase and decrease of net worth of landowners
#show percent growth and decisons they have made
