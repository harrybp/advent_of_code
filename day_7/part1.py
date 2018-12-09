with open('input.txt') as f:
    content = f.readlines()

class Step():
    def __init__(self, letter):
        self.letter = letter
        self.prereqs = []
    def add_prereq(self, letter):
        self.prereqs.append(letter)
    def print(self):
        print(self.letter + str(self.prereqs))

steps = {}
for line in content:
    prereq = line[5]
    if prereq not in steps:
        steps[prereq] = Step(prereq)
    step = line[36]
    if step not in steps:
        steps[step] = Step(step)
    steps[step].add_prereq(prereq)

for i, step in enumerate(steps):
    steps[step].print()

steps_done = []
while len(steps_done) < 26:
    potential_next_steps = []
    for step in steps:
        potential = True
        step_obj = steps[step]
        for prereq in step_obj.prereqs:
            if prereq not in steps_done:
                potential = False
        if potential and step_obj.letter not in steps_done:
            potential_next_steps.append(step_obj.letter)
    potential_next_steps = sorted(potential_next_steps)   
    steps_done += potential_next_steps[0]     
    

result = ''.join(steps_done)
print(result)

        