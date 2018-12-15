import os
import copy
import functools
import sys

class Elf():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type='E'
        self.hp = 200
        self.attack = 19

class Goblin():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.type = 'G'
        self.hp = 200
        self.attack = 3

class Position():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 1


def get_adjacent_positions(creatures, cave):
    positions = []
    for creature in creatures:
        if creature.hp < 1:
            continue
        #Above 
        if cave[creature.x][creature.y-1] == '.':
            positions.append(Position(creature.x,creature.y-1))
        #Below
        if cave[creature.x][creature.y+1] == '.':
            positions.append(Position(creature.x,creature.y+1))
        #Left
        if cave[creature.x-1][creature.y] == '.':
            positions.append(Position(creature.x-1,creature.y))
        #Right
        if cave[creature.x+1][creature.y] == '.':
            positions.append(Position(creature.x+1,creature.y))
    return positions
        


#For ordering carts by y then x
def creature_comparator(a, b):
    if a.x == b.x:
        return a.y - b.y
    else:
        return a.x - b.x

def read_input():
    script_dir = os.path.dirname(__file__)
    with open(script_dir + '/input.txt') as f:
        content = f.readlines()
    cave = []
    elves = []
    goblins = []
    for i in range(len(content)):
        cave.append([])
        row = list(content[i])
        print(row)
        for j in range(len(row)):
            if row[j] == '\n':
                continue
            elif row[j] == 'E':
                elves.append(Elf(i,j))
                cave[i].append('.')
            elif row[j] == 'G':
                goblins.append(Goblin(i,j))
                cave[i].append('.')
            else:
                cave[i].append(row[j])
    return cave, elves, goblins


def print_cave(cave, elves, goblins):
    cavecopy = fill_cave(cave, elves, goblins)    
    for line in cavecopy:
        print(''.join(line))
    for elf in elves:
        print('ELF HP: ' + str(elf.hp))
    for goblin in goblins:
        print('GOB HP: ' + str(goblin.hp))

def fill_cave(cave, elves, goblins):
    cavecopy = copy.deepcopy(cave)
    for elf in elves:
        if elf.hp > 0:
            cavecopy[elf.x][elf.y] = 'E'
    for goblin in goblins:
        if goblin.hp > 0:
            cavecopy[goblin.x][goblin.y] = 'G'  
    return cavecopy

def print_list(points):
    for pos in points:
        print('(' + str(pos.x) + ',' + str(pos.y) +' [' + str(pos.hp) +']) ', end ='' )
    print()

def get_move(a,b, cave):
    path = bfs_shortest_path(cave,a,b)
    if path == None:
        return None, 9999
    else:
        return path[1], len(path)

def is_in(node, list_nodes):
    for item in list_nodes:
        if item.x == node.x and item.y == node.y:
            return True
    return False

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]
    if start.x == goal.x and start.y == goal.y:
        return None
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if not is_in(node, explored):
            neighbours = get_adjacent_positions([node], graph)
            neighbours = sorted(neighbours, key=functools.cmp_to_key(creature_comparator))
            for neighbour in neighbours:

                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour.x == goal.x and neighbour.y == goal.y:
                    return new_path
            explored.append(node)
    return None

def get_number_alive(creatures):
    count = 0
    for creature in creatures:
        if creature.hp > 0:
            count += 1
    return count

def get_neighbours(node, enemys):
    neighbours=[]
    for enemy in enemys:
        if enemy.hp < 1:
            continue
        if enemy.x == node.x:
            if abs(enemy.y - node.y) < 2:
                neighbours.append(enemy)
        if enemy.y == node.y:
            if abs(enemy.x - node.x) < 2:
                neighbours.append(enemy)
    return neighbours

def get_total_hp(units):
    total = 0
    for unit in units:
        if unit.hp > 0:
            total += unit.hp
    return total

def check_elf_dead(elves):
    for elf in elves:
        #print(elf.hp)
        if elf.type == 'E' and elf.hp < 1:
            return True
            #print('hp:' +str(elf.hp))
    return False

def sort_targets(a,b):
    if a.hp == b.hp:
        print('la')
        return creature_comparator(a,b)
    else: 
        return a.hp - b.hp


def test(cave, elves, goblins):
    #cave = copy.deepcopy(cave1)
    #elves = copy.deepcopy(elves1)
    #goblins = copy.deepcopy(goblins1)
    all_units = elves + goblins
    for i in range(5000):
        if check_elf_dead(all_units):
            print('ok')
            return False
        #print()
        #print_cave(cave, elves, goblins)
        #x = input()
        all_units = sorted(all_units, key=functools.cmp_to_key(creature_comparator))
        for unit in all_units:
            if unit.hp < 1:
                continue

            if unit.type == 'E':
                enemy = goblins
            else:
                enemy = elves
                
                

            if len(get_neighbours(unit, enemy)) < 1:
                print('.',end='')
                sys.stdout.flush()
                #print_cave(cave, elves, goblins)
                filled_cave = fill_cave(cave, elves, goblins)
                potential_attacks = get_adjacent_positions(enemy, filled_cave)
                potential_attacks = sorted(potential_attacks, key=functools.cmp_to_key(creature_comparator))
                best_move = None
                shortest = 9999
                for attack in potential_attacks:
                    move, dist = get_move(unit, attack, filled_cave)
                    if move != None:
                        if dist < shortest:
                            shortest = dist
                            best_move = move
                if best_move != None:
                    unit.x = best_move.x
                    unit.y = best_move.y
            
            targets = get_neighbours(unit, enemy)
            if len(targets) > 0:
                print_list(targets)
                targets = sorted(targets, key=functools.cmp_to_key(sort_targets))
                print_list(targets)
                targets[0].hp -= unit.attack
        

        goblins_left = get_number_alive(goblins)
        elves_left = get_number_alive(elves)
        if goblins_left < 1:
            total = get_total_hp(elves)
            print_cave(cave, elves, goblins)
            print(total)
            print(i)
            return True

cave, elves, goblins = read_input()
print_cave(cave, elves, goblins)
done = False

test(cave, elves, goblins)

#print(hit_power)
