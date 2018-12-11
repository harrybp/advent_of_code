import numpy as np
serial_number = 5034
grid_size = 300

def find_power_level(input):
    x = input[0]
    y = input[1]
    rack_id = x + 10
    power_level = rack_id * y
    power_level = power_level + serial_number
    power_level = power_level * rack_id
    power_level = int(str(power_level)[-3]) - 5
    return power_level


grid = np.zeros((grid_size,grid_size),dtype=(int,2))
for i in range(grid_size):
    for j in range(grid_size):
        grid[i][j] = (i+1,j+1)
result = list(map(lambda row: list(map(find_power_level, row)), grid))

def get_three_by_three(grid, x, y):
    return np.sum(grid[x][y:y+3] + grid[x+1][y:y+3] + grid[x+2][y:y+3])

highest_power = 0
highest_x = None
highest_y = None
for i in range(grid_size - 3):
    for j in range(grid_size - 3):
        power = get_three_by_three(result,i,j)
        if power > highest_power:
            highest_power = power
            highest_x = i + 1
            highest_y = j + 1

print(highest_power, highest_x, highest_y)

