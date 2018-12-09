import re
import numpy as np

with open('input.txt') as f:
    content = f.readlines()

def manhattan_dist(ax,ay,bx,by):
    return abs(ax-bx) + abs(ay-by)

#Read in points as [id,x,y]
points = []
for i,line in enumerate(content):
    coords = re.findall('\d+', line)
    x = int(coords[0])
    y = int(coords[1])
    points.append((i,x,y))

#Fill grid with id of closest point
grid = np.zeros((360,360))
for i in range(360):
    for j in range(360):
        closest = 9999999
        closest_id = None
        for point in points:
            dist = manhattan_dist(i,j,point[1],point[2])
            if dist == closest:
                closest_id = -1
            if dist < closest:
                closest = dist
                closest_id = point[0]
        grid[i][j] = closest_id

#Find all infinite spaces
discounted = [-1]
for i in range(360):
    for j in range(360):
        if i == 0 or j == 0 or i == 359 or j == 359:
            if grid[i][j] not in discounted:
                discounted.append(grid[i][j])

#Get the area for each of the valid points
valid_points = {}
for i in range(360):
    for j in range(360):
        value = grid[i][j]
        if value in discounted:
            continue
        if value not in valid_points:
            valid_points[value] = 1
        else:
            valid_points[value] += 1

max_area = 0
for point in valid_points:
    value = valid_points[point]
    if value > max_area:
        max_area = value

print(max_area)