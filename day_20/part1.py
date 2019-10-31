import os
import sys
sys.setrecursionlimit(15000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generate the directed graph from the regex
def solve(regex):
    graph = {}
    stack = []
    x_pos = 0
    y_pos = 0
    for c in regex:
        save_x, save_y = x_pos, y_pos
        if c == 'N':
            y_pos -= 1
        elif c == 'S':
            y_pos += 1
        elif c == 'E':
            x_pos += 1
        elif c == 'W':
            x_pos -= 1
        elif c == '(':
            stack.append((x_pos, y_pos))
        elif c == '|':
            x_pos, y_pos = stack[-1]
        elif c == ')':
            stack.pop()
        if (save_x, save_y) in graph:
            if not (x_pos, y_pos) in graph[(save_x, save_y)]:
                graph[(save_x, save_y)].append((x_pos, y_pos))
        else:
            graph[(save_x, save_y)] = [(x_pos, y_pos)]
        if not (x_pos, y_pos) in graph:
            graph[(x_pos, y_pos)] = []
    return graph

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Shortest path algorithm
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Open file
script_dir = os.path.dirname(__file__)
print(script_dir)
with open(script_dir + 'input.txt') as f:
    regex = f.readlines()[0][:-1]
    graph = solve(regex)
    longest = 0
    for i, g in enumerate(graph):
        print('pathing %d of %d' % (i, len(graph)))
        length = len(find_shortest_path(graph, (0,0), g))
        if length > longest:
            longest = length
    print(longest-1)

