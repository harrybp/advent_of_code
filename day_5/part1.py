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

changed = True
while(changed):
    polymer, changed = collapse(polymer)

print(len(polymer))