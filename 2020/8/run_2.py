import os, sys, re
import copy

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

colours = set()

matches = {}

orig_image = {}

for index, line in enumerate(lines):
    split = line.split()
    instruction = split[0]
    value = split[1]
    orig_image[index] = {"Instruction" : instruction, "Value" : value}

n_inst = len(orig_image)

for i in range(len(orig_image)):
    image = copy.deepcopy(orig_image)
    if image[i]["Instruction"] == 'jmp':
        image[i]["Instruction"] = 'nop'
    elif image[i]["Instruction"] == 'nop':
        image[i]["Instruction"] = 'jmp'

    pc = 0
    acc = 0
    used = []
    while True:
        if pc in used:
#            print('Program broken!')
            break
        if pc == n_inst:
            print('Program finished! {}'.format(acc))
            break

        instruction = image[pc]["Instruction"]
        value = image[pc]["Value"]
        used.append(pc)

        if instruction == 'acc':
            acc += int(value[1:]) * (1 if value[0] == '+' else -1)
            pc += 1
        elif instruction == 'nop':
            pc += 1
            continue
        elif instruction == 'jmp':
            pc += int(value[1:]) * (1 if value[0] == '+' else -1)

