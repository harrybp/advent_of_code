import numpy as np
import functools
import copy

class Cart():
    def __init__(self, x, y, direction):
        self.destroyed = False
        self.x = x
        self.y = y
        self.direction = direction
        self.next_turn = 'left'

    def advance(self, tracks):
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

#Read in input from file
def get_input(filename):
    with open(filename) as f:
        content = f.readlines()
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
    return tracks, carts

#Prints the current state, for debugging
def print_tracks(tracks, carts):
    tracks_and_carts = copy.deepcopy(tracks)
    for cart in carts:
        if cart.destroyed:
            continue
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

#For ordering carts by y then x
def cart_comparator(a, b):
    if a.y == b.y:
        return a.x - b.x
    else:
        return a.y - b.y

#Destroy any crashed carts
def check_crashes(carts, cart):
    crashed = False
    for i in range(len(carts)):
        if i == carts.index(cart):
            continue
        if carts[i].x == cart.x and carts[i].y == cart.y and not cart.destroyed and not carts[i].destroyed:
                crashed = True
                carts[i].destroyed = True
                cart.destroyed = True
    return crashed


tracks, carts = get_input('input.txt')
while True:
    #Advance carts
    carts = sorted(carts, key=functools.cmp_to_key(cart_comparator))
    for cart in carts:
        cart.advance(tracks)
        crashed = check_crashes(carts, cart)
    #Check how many havent crashed
    alive_carts = 0
    for cart in carts:
        if not cart.destroyed:
            alive_carts += 1
    if alive_carts < 2:
        break
    
#Print result
for cart in carts:
    if not cart.destroyed:
        print(cart.y, cart.x)