import os, sys, math
import numpy as np
import matplotlib.pyplot as plt

#filename = "input_test2.txt"
filename = "input_final.txt"

with open(filename) as file:
    lines = file.readlines()

#on x=-30..21,y=-8..43,z=-13..34

class Rule:
    def __init__(self, value, minX, maxX, minY, maxY, minZ, maxZ):
        self.value = value
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
        self.taken = False

        self.idx = []
        self.values = []
        self.minXs = []
        self.maxXs = []
        self.minYs = []
        self.maxYs = []
        self.minZs = []
        self.maxZs = []

    def __str__(self):
        return "x={}..{}, y={}..{}, z={}..{}".format(self.minX, self.maxX, self.minY, self.maxY, self.minZ, self.maxZ)

    def overlap(self, other, idx):
        xOverlap = False
        for i in range(other.minX, other.maxX + 1):
            if i in range(self.minX, self.maxX + 1):
                xOverlap = True
                break

        yOverlap = False
        for i in range(other.minY, other.maxY + 1):
            if i in range(self.minY, self.maxY + 1):
                yOverlap = True
                break

        zOverlap = False
        for i in range(other.minZ, other.maxZ + 1):
            if i in range(self.minZ, self.maxZ + 1):
                zOverlap = True
                break

        if xOverlap and yOverlap and zOverlap:
            other.taken = True
            self.idx.append(idx)
            self.values.append(other.value)
            self.minXs.append(other.minX)
#            self.minX = min(self.minX, other.minX)
            self.maxXs.append(other.maxX)
#            self.maxX = max(self.maxX, other.maxX)

            self.minYs.append(other.minY)
#            self.minY = min(self.minY, other.minY)
            self.maxYs.append(other.maxY)
#            self.maxY = max(self.maxY, other.maxY)

            self.minZs.append(other.minZ)
#            self.minZ = min(self.minZ, other.minZ)
            self.maxZs.append(other.maxZ)
#            self.maxZ = max(self.maxZ, other.maxZ)
            return True

        return False

    def count(self, ignore):
        xSpan = self.maxX + 1 - self.minX
        ySpan = self.maxY + 1 - self.minY
        zSpan = self.maxZ + 1 - self.minZ

        grid = [1] * xSpan * ySpan * zSpan

        print(xSpan)
        print(ySpan)
        print(zSpan)

        for index in range(len(self.values)):
            for x in range(self.minXs[index], self.maxXs[index] + 1):
                if x < self.minX or x > self.minX + 1:
                    continue
                for y in range(self.minYs[index], self.maxYs[index] + 1):
                    if y < self.minY or y > self.minY + 1:
                        continue
                    for z in range(self.minZs[index], self.maxZs[index] + 1):
                        if z < self.minZ or z > self.minZ + 1:
                            continue
                        value = self.values[index]
                        if self.idx[index] in ignore:
                            value = 0
                        number = (x + abs(self.minX)) + (y + abs(self.minY)) * xSpan + (z + abs(self.minZ)) * ySpan * xSpan
                        grid[number] = value

        for rule in ignore:
            if self.overlap(rule):
                for x in range(rule.minX, rule.maxX + 1):
                    for y in range(rule.minY, rule.maxY + 1):
                        for z in range(rule.minZ, rule.maxZ + 1):
                            number = (x + abs(self.minX)) + (y + abs(self.minY)) * xSpan + (z + abs(self.minZ)) * ySpan * xSpan
                            if number in grid:
                                grid[number] = 0

        count = 0

        for i in grid:
            if i == 1:
                count += 1

        print("Count {}".format(count))


rules = []

for line in lines:
    line = line.strip()
    split = line.split()
    second = split[1].split(",")
    print("Rule {}".format(second))

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

    rules.append(Rule(value, minX, maxX, minY, maxY, minZ, maxZ))

ignore = []

for x in range(2):
    print("Iteration {} number of rules {}".format(x, len(rules)))
    for i in [0,1]: #range(len(rules)):
        for j in range(i + 1, len(rules)):
            overlap = rules[i].overlap(rules[j])
            if overlap:
                print("{} {} Overlap {}".format(i, j, overlap))
        rules[i].count(ignore)
        ignore.append(i)
