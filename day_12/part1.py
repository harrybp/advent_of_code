with open('input.txt') as f:
        content = f.readlines()

initial_state = content[0].splitlines()[0].split(' ')[2]
mappings = {}
for i in range(2, len(content)):
    mapping = content[i].splitlines()[0].split(' ')
    mappings[mapping[0]] = mapping[2]
    print(mapping)

def step(state, mappings):
    new_state = '.' * len(state)
    for key in mappings:
        location = state.find(key)
        plus = 0
        while location > -1:
            new_state = new_state[:location + 2 + plus] + mappings[key] + new_state[location + 3 + plus:]
            plus = plus + location + 1
            location = state[plus:].find(key)
    return new_state

initial_state = '.'*10 + initial_state + '.'*30 #Pad the state with 10
print('0' + initial_state)
for i in range(20):
    initial_state = step(initial_state, mappings)
    print(str(i+1) + initial_state[2:-2])

#SUm up plant numbers
total = 0
for i in range(len(initial_state)):
    if initial_state[i] == '#':
        total += (i-10)

print(total)


