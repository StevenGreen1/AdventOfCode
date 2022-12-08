import os, sys
import numpy as np

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

count = 0

mod = np.convolve(lines, [1,1,1], 'valid')

for index in range(1,len(mod)):
    if mod[index] - mod[index - 1] > 0:
        count += 1

print(count)

