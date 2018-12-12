with open('input.txt') as f:
        content = f.readlines()

#Read in data
initial_state = content[0].splitlines()[0].split(' ')[2]
mappings = {}
for i in range(2, len(content)):
    mapping = content[i].splitlines()[0].split(' ')
    mappings[mapping[0]] = mapping[2]

#Step forward by one generation
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

initial_state = '.'*10 + initial_state + '.' * 30 #Pad the state with 10
generations = 50000000000
previous_state = initial_state
sliding_starts = None #At some point the pattern remains the same and just slides to the right
for i in range(generations):
    initial_state = step(initial_state, mappings) + '.'
    if previous_state == initial_state[1:]:
        sliding_starts = i+1
        break
    previous_state = initial_state

initial_state = initial_state[10:] #Remove padding
total = 0
for i in range(len(initial_state)):
    if initial_state[i] == '#':
        total += (i + (generations-sliding_starts))

print(total)
