import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]

horiz = 0
depth = 0
aim = 0

#down X increases your aim by X units.
#up X decreases your aim by X units.
#forward X does two things:
#It increases your horizontal position by X units.
#It increases your depth by your aim multiplied by X.

for line in lines:
    if line[0] == 'forward':
        horiz += int(line[1])
        depth += int(line[1]) * aim
    elif line[0] == 'backwards':
        horiz -= int(line[1])
    elif line[0] == 'up':
        #depth -= int(line[1])
        aim -= int(line[1])
    elif line[0] == 'down':
        #depth += int(line[1])
        aim += int(line[1])
    else:
        print(line[0])
print('Horiz {} x Depth {} = {}'.format(horiz, depth, horiz*depth))


