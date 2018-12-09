import numpy as np
import re 

fabric = np.zeros((1000,1000))

def add_claim(fabric, x, y, w, h):
    for i in range(x, x+w):
        for j in range(y, y+h):
            fabric[j][i] += 1
    return fabric

with open('input.txt') as f:
    content = f.readlines()

for line in content:
    line = re.findall('\d+', line)
    fabric = add_claim(fabric, int(line[1]), int(line[2]), int(line[3]), int(line[4]))

def verify_claim(fabric, x, y, w, h):
    overlaps = False
    for i in range(x, x+w):
        for j in range(y, y+h):
            if fabric[j][i] > 1:
                overlaps = True
                break
    return overlaps

for line in content:
    line = re.findall('\d+', line)
    overlaps = verify_claim(fabric, int(line[1]), int(line[2]), int(line[3]), int(line[4]))
    if not overlaps:
        print(line[0])
        