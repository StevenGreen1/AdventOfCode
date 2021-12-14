import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

count = 0

for index in range(1,len(lines)):
    if lines[index] - lines[index - 1] > 0:
        count += 1

print(count)

