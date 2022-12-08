import os, sys, re, copy, math
import numpy as np

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

x = 0
y = 0
dir = (1, 0)

way_point = (10, 1)

for line in lines:
    letter = line[0]
    n_steps = int(line[1:])
    step = (0, 0)

    if letter == "N":
        way_point = (way_point[0], way_point[1] + n_steps) 
    elif letter == "S":
        way_point = (way_point[0], way_point[1] - n_steps) 
    elif letter == "E":
        way_point = (way_point[0] + n_steps, way_point[1]) 
    elif letter == "W":
        way_point = (way_point[0] - n_steps, way_point[1]) 
    elif letter == "F":
        step_x = n_steps * (way_point[0] - x)
        x += step_x
        step_y = n_steps * (way_point[1] - y)
        y += step_y
        way_point = (way_point[0] + step_x, way_point[1] + step_y)
    elif letter == "L" or letter == "R":
        rel_x = way_point[0] - x
        rel_y = way_point[1] - y
        theta = n_steps if letter == "L" else -n_steps
        new_x = rel_x * math.cos(math.radians(theta)) - rel_y * math.sin(math.radians(theta))
        new_y = rel_x * math.sin(math.radians(theta)) + rel_y * math.cos(math.radians(theta))
        way_point = (x + new_x, y + new_y)
    else:
        print("Problem")

    print(line)
    print(x, y, way_point)

print(abs(x) + abs(y))
