import os, sys, re

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []

for index, line in enumerate(lines):
    numbers.append(int(line))

span = 25
key = 1398413738

for span in range(2, len(numbers)):
    for start in range(0, len(numbers) - span):
        active_sum = sum(numbers[start:start + span])
        if active_sum == key:
            print(numbers[start:start + span])
            print(min(numbers[start:start + span]) + max(numbers[start:start + span]))


