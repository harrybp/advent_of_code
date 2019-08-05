import os
import re
import numpy as np
script_dir = os.path.dirname(__file__)

active_water = []
first_water = [500,0]
active_water.append(first_water)

def get_bounds(content):
    smallest_x = 99999999
    largest_x = 0
    smallest_y = 99999999
    largest_y = 0

    for line in content:
        parts = re.findall(r'\d+', line)
        parts = list(map(int, parts))

        if line[0] == 'x':
            smallest_x = min(smallest_x, parts[0])
            largest_x = max(largest_x, parts[0])
            smallest_y = min(smallest_y, parts[1])
            largest_y = max(largest_y, parts[1])
            smallest_y = min(smallest_y, parts[2])
            largest_y = max(largest_y, parts[2])
            
        if line[0] == 'y':
            smallest_y = min(smallest_y, parts[0])
            largest_y = max(largest_y, parts[0])
            smallest_x = min(smallest_x, parts[1])
            largest_x = max(largest_x, parts[1])
            smallest_x = min(smallest_x, parts[2])
            largest_x = max(largest_x, parts[2])
    print("X: [%d:%d], Y: [%d:%d]" % (smallest_x, largest_x, smallest_y, largest_y))
    return [smallest_x, largest_x, smallest_y, largest_y]

with open(os.path.join(script_dir, 'input.txt')) as f:
        content = f.readlines()
        bounds = get_bounds(content)
        x_offset = bounds[0]

        #Initialise map array and add source
        map_array = np.zeros((bounds[1] - bounds[0] + 4, bounds[3] + 1))
        map_array[500-x_offset][0] = 2

        #Fill array
        for line in content:
            parts = re.findall(r'\d+', line)
            parts = list(map(int, parts))
            if line[0] == 'x':
                for i in range(parts[1], parts[2] + 1):
                    map_array[parts[0] - x_offset][i] = 1
            if line[0] == 'y':
                for i in range(parts[1], parts[2] + 1):
                    map_array[i-x_offset][parts[0]] = 1        



def print_map(map_array, to_file=False):
    map_string = ''
    for i in range(len(map_array[0])):
        for j in range(len(map_array)):
            if map_array[j][i] == 0:
                map_string += ' '
            if map_array[j][i] == 1:
                map_string += '#'
            if map_array[j][i] == 2:
                map_string += '+'
            if map_array[j][i] == 3:
                map_string += '|'
            if map_array[j][i] == 4:
                map_string += '~'
        map_string += '\n'

    if to_file:
        f= open("guru99.txt","w+")
        f.write(map_string)
        f.close() 
    else:
        print(map_string)


def count_water(map_array):
    water_count = 0
    for i in range(len(map_array[0])):
        for j in range(len(map_array)):
            if map_array[j][i] == 4:
                if i <= bounds[3] and i >= bounds[2]:
                    water_count += 1
    return water_count

def next():
    current_water = active_water.pop()

    #Bounds check
    if current_water[1] >= len(map_array[0])-1:
        return

    if map_array[current_water[0]-x_offset][current_water[1] + 1] == 3:
        return

    #Easy flow down
    if map_array[current_water[0]-x_offset][current_water[1] + 1] == 0:
        map_array[current_water[0]-x_offset][current_water[1] + 1] = 3
        current_water[1] += 1
        active_water.append(current_water)

    else:
        #Go left to find wall
        current_x = current_water[0]
        did_spill = False

        while(map_array[current_x - x_offset][current_water[1]] != 1):
            if(map_array[current_x - x_offset][current_water[1]+1] != 0 and map_array[current_x - x_offset][current_water[1]+1] != 3):
                current_x-=1
            else:
                did_spill = True
                active_water.append([current_x, current_water[1]])
                current_x-=1
                break
        lowest_x = current_x

        #Go right to find wall
        current_x = current_water[0]
        while(map_array[current_x - x_offset][current_water[1]] != 1):
            if(map_array[current_x - x_offset][current_water[1]+1] != 0 and map_array[current_x - x_offset][current_water[1]+1] != 3):
                current_x+=1
            else:
                did_spill = True
                active_water.append([current_x, current_water[1]])
                current_x+=1
                break
        highest_x = current_x

        #Fill in
        for i in range(lowest_x + 1, highest_x):
            if not did_spill:
                map_array[i - x_offset][current_water[1]] = 4
            else:
                map_array[i - x_offset][current_water[1]] = 3

        if not did_spill:
            current_water[1] -= 1
            active_water.append(current_water)


while len(active_water) > 0:
    next()
print_map(map_array, to_file=True)
print(count_water(map_array))

