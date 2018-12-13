import numpy as np
import functools
import copy

with open('input.txt') as f:
        content = f.readlines()

def print_tracks(tracks, carts):
    tracks_and_carts = copy.deepcopy(tracks)
    for cart in carts:
        if cart.direction == 0:
            tracks_and_carts[cart.x][cart.y] = '^'
        elif cart.direction == 2:
            tracks_and_carts[cart.x][cart.y] = 'v'
        elif cart.direction == 3:
            tracks_and_carts[cart.x][cart.y] = '<'
        elif cart.direction == 1:
            tracks_and_carts[cart.x][cart.y] = '>'
    for i in range(len(tracks_and_carts)):
        print(''.join(tracks_and_carts[i]))

#direction          turn left   turn right
#   up      0       -1          +1
#   right   1       -1          +1
#   down    2       -1          +1
#   left    3       -1          +1
class Cart():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_turn = 'left'

    def advance(self):
        if self.direction == 1:#Right
            self.y += 1
            if tracks[self.x][self.y] == '/':
                self.direction = 0
            elif tracks[self.x][self.y] == '\\':
                self.direction = 2
        elif self.direction == 3: #Left
            self.y -= 1
            if tracks[self.x][self.y] == '/':
                self.direction = 2
            elif tracks[self.x][self.y] == '\\':
                self.direction = 0
        elif self.direction == 0: #Up
            self.x -= 1
            if tracks[self.x][self.y] == '/':
                self.direction = 1
            elif tracks[self.x][self.y] == '\\':
                self.direction = 3
        elif self.direction == 2: #Down
            self.x += 1
            if tracks[self.x][self.y] == '/':
                self.direction = 3
            elif tracks[self.x][self.y] == '\\':
                self.direction = 1
        if tracks[self.x][self.y] == '+':
            if self.next_turn == 'left':
                self.next_turn = 'straight'
                self.direction -= 1
            elif self.next_turn == 'right':
                self.next_turn = 'left'
                self.direction += 1 
            else:
                self.next_turn = 'right'
            self.direction = self.direction % 4

crashed = False
def cart_comparator(a, b):
    global crashed
    if a.y == b.y:
        return a.x - b.x
    else:
        return a.y - b.y

def check_crashed(carts, cart):
    crashed = False
    for i in range(len(carts)):
        if i == carts.index(cart):
            continue
        if carts[i].x == cart.x and carts[i].y == cart.y:
                crashed = True
                print('CRASH AT: ' + str(carts[i].y) + ',' + str(carts[i].x))
    return crashed

#Read in input
tracks = []
carts = []
for i in range(len(content)):
    tracks.append([])
    for j in range(len(content[i])):
        if content[i][j] != '\n':
            if content[i][j] == '<':
                carts.append(Cart(i,j,3))
                tracks[i].append('-')
            elif content[i][j] == '>':
                carts.append(Cart(i,j,1))
                tracks[i].append('-')
            elif content[i][j] == '^':
                carts.append(Cart(i,j,0))
                tracks[i].append('|')
            elif content[i][j] == 'v':
                carts.append(Cart(i,j,2))
                tracks[i].append('|')
            else:
                tracks[i].append(content[i][j])

print_tracks(tracks, carts)
carts = sorted(carts, key=functools.cmp_to_key(cart_comparator))
while not crashed:
    for cart in carts:
        cart.advance()
        crashed = check_crashed(carts, cart)
    
    #print_tracks(tracks, carts)
    carts = sorted(carts, key=functools.cmp_to_key(cart_comparator))
    #x = input()
    

