import itertools
import os
import re
import copy
script_dir = os.path.dirname(__file__)

with open(script_dir + '/input1.txt') as f:
        content = f.readlines()

#Add register
def addr(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] + inputs[instruction[2]]
    return inputs

#Add immediate
def addi(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] + instruction[2]
    return inputs

#Multiply register
def mulr(inputs, instruction):
    inputs[instruction[3]] = int(inputs[instruction[1]] * inputs[instruction[2]])
    return inputs

#Multiply immediate
def muli(inputs, instruction):
    inputs[instruction[3]] = int(inputs[instruction[1]] * instruction[2])
    return inputs

#AND register
def banr(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] & inputs[instruction[2]]
    return inputs

#AND immediate
def bani(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] & instruction[2]
    return inputs

#OR register
def borr(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] | inputs[instruction[2]]
    return inputs

#OR immediate
def bori(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]] | instruction[2]
    return inputs

#Set register
def setr(inputs, instruction):
    inputs[instruction[3]] = inputs[instruction[1]]
    return inputs

#Set immediate
def seti(inputs, instruction):
    inputs[instruction[3]] = instruction[1]
    return inputs

#Greater than immediate-register
def gtir(inputs, instruction):
    if instruction[1] > inputs[instruction[2]]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

#Greater than register-immediate
def gtri(inputs, instruction):
    if inputs[instruction[1]] > instruction[2]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

#Greater than register-register
def gtrr(inputs, instruction):
    if inputs[instruction[1]] > inputs[instruction[2]]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

#Equal to immediate-register
def eqir(inputs, instruction):
    if instruction[1] == inputs[instruction[2]]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

#Equal to register-immediate
def eqri(inputs, instruction):
    if inputs[instruction[1]] == instruction[2]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

#Equal to register-register
def eqrr(inputs, instruction):
    if inputs[instruction[1]] == inputs[instruction[2]]:
        inputs[instruction[3]] = 1
    else: 
        inputs[instruction[3]] = 0
    return inputs

def test_methods(opcode, methods, content):
    found = 0
    method_found = None
    for method in methods:
        is_this = True
        for i in range(0, len(content),4):
            inputs = list(map(int, re.findall('\d+', content[i])))
            instruction = list(map(int, re.findall('\d+', content[i+1])))
            outputs =  list(map(int, re.findall('\d+', content[i+2])))
            if instruction[0] != opcode:
                continue
            result = method(copy.deepcopy(inputs), instruction)
            if result != outputs:
                is_this = False
                break
        if is_this:
            found += 1
            method_found = method

    return found, method_found

def print_mappings(mappings):
    for i in sorted(mappings):
        print(i, mappings[i].__name__)

print('ok')
methods = [bani, banr, muli, gtir,bori, setr, eqrr, mulr, gtrr, seti, gtri, eqri, addi, borr, eqir, addr]
done = []
mappings = {}
while len(methods) > 0:
    for i in range(16):
        if i in done:
            continue
        found, method = test_methods(i, methods, content)
        if found == 1:
            mappings[i] = method
            methods.remove(method)
            done.append(i)
    print_mappings(mappings)

with open(script_dir + '/input2.txt') as f:
        content = f.readlines()

registers = [0,0,0,0]
for line in content:
    instruction = list(map(int, re.findall('\d+', line)))
    method = mappings[instruction[0]]
    registers = method(registers, instruction)

print(registers)
