import os, sys, re

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []

for index, line in enumerate(lines):
    numbers.append(int(line))

numbers = sorted(numbers)
print(numbers)

def isValidList(initial_list):
    counter = {}
    for index in range(0,len(initial_list)):
        gap = 0
        if index == 0:
            gap = initial_list[index]
        else:
            gap = initial_list[index] - initial_list[index - 1]

        if gap in counter:
            counter[gap] += 1
        else:
            counter[gap] = 1

    if 3 in counter:
        counter[3] += 1
    else:
        counter[3] = 1

    print(counter)
    print(counter[3] * counter[1])

isValidList(numbers)
