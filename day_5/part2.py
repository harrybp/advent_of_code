import re
from string import ascii_lowercase
with open('input.txt') as f:
    polymer = f.readlines()[0][:-1]

def will_react(a,b):
    return a.lower() == b.lower() and not a == b

def collapse(polymer):
    prev = polymer[0]
    changed = False
    for i in range(1,len(polymer)):
        if will_react(polymer[i], prev):
            polymer = polymer[:i-1] + polymer[i+1:]
            changed = True
            break
        prev = polymer[i]
    return polymer, changed

def get_fully_collapsed_length(polymer):
    changed = True
    while(changed):
        polymer, changed = collapse(polymer)
    return len(polymer)

shortest_len = 99999999999
for character in ascii_lowercase:
    print('Testing without ' + character)
    substitute = '[' + character + character.upper() + ']'
    polymer_substituted = re.sub(substitute, '', polymer)
    poly_length = get_fully_collapsed_length(polymer_substituted)
    print('Length: ' + str(poly_length))
    if poly_length < shortest_len:
        shortest_len = poly_length

print(shortest_len)