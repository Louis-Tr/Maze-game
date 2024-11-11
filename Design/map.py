import random

# Initialize the map as a 30x30 matrix with all 0s (wall tiles)
map_size = 30
map = [[0 for _ in range(map_size)] for _ in range(map_size)]

# Function to check if a cell is within the map boundaries
def is_within_map(x, y):
    return 0 <= x < map_size and 0 <= y < map_size

# Function to count the number of adjacent ground tiles
def count_adjacent_ground(x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            if is_within_map(new_x, new_y) and map[new_x][new_y] == 1:
                count += 1
    return count

# Randomly place wall tiles (0s) on the map
for x in range(1, map_size - 1):
    for y in range(1, map_size - 1):
        if random.random() < 0.3:
            map[x][y] = 0
        else:
            map[x][y] = 1

# Ensure that all ground tiles are connected and have at least 2 adjacent ground tiles
for _ in range(1000):
    for x in range(1, map_size - 1):
        for y in range(1, map_size - 1):
            if map[x][y] == 1 and count_adjacent_ground(x, y) < 2:
                map[x][y] = 0
            elif map[x][y] == 0 and count_adjacent_ground(x, y) >= 2:
                map[x][y] = 0

# Print the generated map
for row in map:
    print(row)



