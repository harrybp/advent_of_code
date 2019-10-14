import os
import re
import copy
script_dir = os.path.dirname(__file__)

with open(script_dir + '/input.txt') as f:
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

methods = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
print(len(methods))

registers = [0, 0, 0, 0, 0, 0]

ip_reg = 3
ip = 0
print(registers)
while ip < len(content)-1:
    
    registers[ip_reg] = ip
    line = content[ip+1].split()
    for j in range(1,4):
        line[j] = int(line[j])
    #print(line)
    operation = line[0]
    registers = locals()[operation](registers, line)
    ip = registers[ip_reg]
    ip += 1
print(registers)

    

