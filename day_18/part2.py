import os
import numpy as np
script_dir = os.path.dirname(__file__)

size_i = 50
size_j = 50
woodland = np.zeros((size_i,size_j))
woodland = woodland.astype(int)

with open(os.path.join(script_dir, 'input.txt')) as f:
        content = f.readlines()
        for i in range(size_i):
            for j in range(size_j):
                if content[i][j] == '.':
                    woodland[i][j] = 0
                if content[i][j] == '|':
                    woodland[i][j] = 1
                if content[i][j] == '#':
                    woodland[i][j] = 2
                
def print_woodland(woodland):
    for i in range(size_i):
            for j in range(size_j):
                if woodland[i][j] == 0:
                    print('.', end='')
                if woodland[i][j] == 1:
                    print('|', end='')
                if woodland[i][j] == 2:
                    print('#', end='')
            print()

def calculate_next(woodland, i, j):
    count = [0, 0, 0]
    if i > 0 and j > 0: # NW
        count[woodland[i-1][j-1]]+=1
    if i < size_i -1 and j < size_j - 1: #SE
        count[woodland[i+1][j+1]] += 1
    if i > 0 and j < size_j - 1: # NE
        count[woodland[i-1][j+1]] += 1
    if i < size_i - 1 and j > 0: # SW
        count[woodland[i+1][j-1]] += 1
    if i > 0:   # N
        count[woodland[i-1][j]] += 1
    if i < size_i - 1: #S
        count[woodland[i+1][j]] += 1
    if j > 0: #W
        count[woodland[i][j-1]] += 1
    if j < size_j - 1:
        count[woodland[i][j+1]] += 1

    if woodland[i][j] == 0:
        if count[1] >= 3:
            return 1
    if woodland[i][j] == 1:
        if count[2] >= 3:
            return 2
    if woodland[i][j] == 2:
        if count[2] < 1 or count[1] < 1:
            return 0
    return woodland[i][j]

def next(woodland):
    new_woodland = np.copy(woodland)
    for i in range(size_i):
        for j in range(size_j):
            new_woodland[i][j] = calculate_next(woodland,i,j)
    return new_woodland

def count_total(woodland):
    count = [0, 0, 0]
    for i in range(size_i):
        for j in range(size_j):
            count[woodland[i][j]] += 1
    return count[1] * count[2]


print_woodland(woodland)
for i in range(2120): #Repeats every 28 starting at 2111, so 2120 == 100000000
    print(i)
    woodland = next(woodland)
print()
print_woodland(woodland)
print(count_total(woodland))
