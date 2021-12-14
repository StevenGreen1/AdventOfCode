import os, sys, copy
import matplotlib.pyplot as plt
import numpy as np

#filename = "input_test.txt"
filename = "input_final.txt"

folds = []
dotsX = []
dotsY = []

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if 'fold' in line:
            folds.append(line)
        elif line == '':
            continue
        else:
            split = [int(val) for val in line.split(',')]
            dotsX.append(split[0])
            dotsY.append(split[1])

def make_fold(dots, split):
    new_dots = []
    for dot in dots:
        if dot > split:
            new_dots.append(2 * split - dot)
        else:
            new_dots.append(dot)
    return new_dots

for fold in folds:
    split = int(fold.split('=')[1])
    points = set()
    if 'x' in fold:
        dotsX = make_fold(dotsX, split)
        for idx, x in enumerate(dotsX):
            points.add((x, dotsY[idx])) 
    else:
        dotsY = make_fold(dotsY, split)
        for idx, y in enumerate(dotsY):
            points.add((dotsX[idx], y))

#dotsX = [-dot for dot in dotsX]
dotsY = [-dot for dot in dotsY]
plt.scatter(dotsX, dotsY)
#plt.hist2d(dotsX, dotsY, bins=(38, 10))
plt.show()
