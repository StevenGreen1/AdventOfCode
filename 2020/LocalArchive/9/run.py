import os, sys, re

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []

for index, line in enumerate(lines):
    numbers.append(int(line))

print(numbers)
span = 25

for start in range(span, len(numbers)):
    target = numbers[start]
    possibilities = numbers[start-span:start]

    subtracted = [target - i for i in possibilities]
    answers = list(set(subtracted) & set(possibilities))

    if len(answers) == 0:
        print(target)
        print(possibilities)
        print(subtracted)
        print(answers)
        sys.exit()
