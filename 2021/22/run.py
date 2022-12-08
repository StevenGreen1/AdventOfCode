import os, sys, math
import numpy as np
import matplotlib.pyplot as plt

#filename = "input_test2.txt"
filename = "input_final.txt"

with open(filename) as file:
    lines = file.readlines()

rules = { "Set" : [], "MinX" : [], "MaxX" : [], "MinY" : [], "MaxY" : [], "MinZ" : [], "MaxZ" : []}

#on x=-30..21,y=-8..43,z=-13..34

size = 100
grid = [0] * size * size * size

for line in lines:
    line = line.strip()
    split = line.split()
    second = split[1].split(",")
    print(i"Rule {}".format(second))

    value = 1 if split[0] == "on" else 0

    x = second[0][2:]
    y = second[1][2:]
    z = second[2][2:]

    minX = int(x.split("..")[0])
    maxX = int(x.split("..")[1])
    minY = int(y.split("..")[0])
    maxY = int(y.split("..")[1])
    minZ = int(z.split("..")[0])
    maxZ = int(z.split("..")[1])

    if maxX < -size or maxX > size:
        continue
    if maxY < -size or maxY > size:
        continue
    if maxZ < -size or maxZ > size:
        continue

#    print("X:{}..{}, Y:{}..{}, Z: {}..{}".format(minX, maxX, minY, maxY, minZ, maxZ))

    for x in range(minX, maxX+1):
        x = x + size
        for y in range(minY, maxY+1):
            y = y + size
            for z in range(minZ, maxZ+1):
                z = z + size
                number = x + size * y + z * size * size
#                print("{},{},{} = {}".format(x-50,y-50,z-50,number))
                if number < size * size * size and number >= 0:
                    grid[number] = value

count = 0
for i in grid:
    if i == 1:
        count += 1

print(count)
