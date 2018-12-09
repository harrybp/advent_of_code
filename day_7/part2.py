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

def get_step_time(letter):
    return ord(letter) - 4

steps_done = []
steps_begun = []
workers = [
    [0,None],
    [0,None],
    [0,None],
    [0,None],
    [0,None]
]
total_time = -1
while len(steps_done) < 26:
    total_time += 1

    #Reduce time remaining for workers
    for worker in workers:
        worker[0] -= 1

    #Get tasks completed this second
    completed_this_second = []
    for worker in workers:
        if worker[0] < 1 and worker[1]:
            completed_this_second += worker[1]
            worker[1] = None
    completed_this_second = sorted(completed_this_second)
    steps_done += completed_this_second

    potential_next_steps = []
    for step in steps:
        potential = True
        step_obj = steps[step]
        for prereq in step_obj.prereqs:
            if prereq not in steps_done:
                potential = False
        if potential and step_obj.letter not in steps_begun:
            potential_next_steps.append(step_obj.letter)
    potential_next_steps = sorted(potential_next_steps)   
    print(potential_next_steps)
    
    for worker in workers:
        if len(potential_next_steps) < 1:
            break
        if worker[0] < 1:
            worker[0] = get_step_time(potential_next_steps[0])
            worker[1] = potential_next_steps[0]
            steps_begun.append(potential_next_steps[0])
            potential_next_steps = potential_next_steps[1:]
            
    

result = ''.join(steps_done)
print(result)
print(total_time)

        