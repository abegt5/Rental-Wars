class City(object):
    def __init__(self, size=50):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.attractions = []

    def add_building(self, building):
        x, y = building.location
        self.grid[x][y] = building

    def add_attraction(self, attraction):
        self.attractions.append(attraction)
        # update nearby buildings' value based on attraction's influence radius
     

    def get_building(self, x, y):
        return self.grid[x][y]
    
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
