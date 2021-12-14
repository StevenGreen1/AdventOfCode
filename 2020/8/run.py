import os, sys, re

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

colours = set()

matches = {}

image = {}

for index, line in enumerate(lines):
    split = line.split()
    instruction = split[0]
    value = split[1]
    image[index] = {"Instruction" : instruction, "Value" : value}

pc = 0
acc = 0

used = []

while True:
    if pc in used:
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

print(acc)
