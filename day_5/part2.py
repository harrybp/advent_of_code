import re
from string import ascii_lowercase
with open('input.txt') as f:
    polymer = f.readlines()[0][:-1]

def will_react(a,b):
    return a.lower() == b.lower() and not a == b

def collapse(polymer):
    output = []
    output.append(polymer[0])
    for i in range(1,len(polymer)):
        if len(output) > 0:
            top_of_stack = output[-1]
        if len(output) > 0 and will_react(top_of_stack, polymer[i]):
            output.pop()
        else:
            output.append(polymer[i])
    return output

def get_fully_collapsed_length(polymer):
    polymer  = collapse(polymer)
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