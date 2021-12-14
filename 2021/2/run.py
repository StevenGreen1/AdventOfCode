import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]

horiz = 0
depth = 0

for line in lines:
    if line[0] == 'forward':
        horiz += int(line[1])
    elif line[0] == 'backwards':
        horiz -= int(line[1])
    elif line[0] == 'up':
        depth -= int(line[1])
    elif line[0] == 'down':
        depth += int(line[1])
    else:
        print(line[0])
print('Horiz {} x Depth {} = {}'.format(horiz, depth, horiz*depth))


