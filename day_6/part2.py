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
        dist = 0
        for point in points:
            dist += manhattan_dist(i,j,point[1],point[2])
        if dist < 10000:
            grid[i][j] = 1

print(np.sum(grid))