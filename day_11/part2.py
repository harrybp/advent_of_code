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

def get_square_total(grid, x, y, size):
    total = []
    for i in range(size):
        total += grid[x+i][y:y+size]
    return np.sum(total)

def find_highest_power_for_size(result, c):
    highest_power = 0
    highest_x = None
    highest_y = None
    for i in range(grid_size-c):
        for j in range(grid_size-c):
            power = get_square_total(result,i,j,c)
            if power > highest_power:
                highest_power = power
                highest_x = i+1
                highest_y = j+1
    return highest_power, highest_x, highest_y

highest_power = 0
highest_x = None
highest_y = None
highest_size = 0
for size in range(0,300):
    high,x,y = find_highest_power_for_size(result, size)
    if high > highest_power:
        highest_power = high
        highest_x = x
        highest_y = y
        highest_size = size    
    print(highest_power, highest_x, highest_y, highest_size)   
          