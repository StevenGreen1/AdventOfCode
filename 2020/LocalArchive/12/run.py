import os, sys, re, copy, math
import numpy as np

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

x = 0
y = 0
dir = (1, 0)

for line in lines:
    letter = line[0]
    n_steps = int(line[1:])
    step = (0, 0)

    if letter == "N":
        step = (0, 1)
    elif letter == "S":
        step = (0, -1)
    elif letter == "E":
        step = (1, 0)
    elif letter == "W":
        step = (-1, 0)
    elif letter == "F":
        step = dir
    elif letter == "L" or letter == "R":
        theta = n_steps if letter == "L" else -n_steps
        new_x = int(dir[0] * math.cos(math.radians(theta)) - dir[1] * math.sin(math.radians(theta)))
        new_y = int(dir[0] * math.sin(math.radians(theta)) + dir[1] * math.cos(math.radians(theta)))
        dir = (new_x, new_y)
        continue
    else:
        print("Problem")

    x += n_steps * step[0]
    y += n_steps * step[1]

    print(x, y)
