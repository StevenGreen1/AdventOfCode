import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

answers = set()
sum = 0
for line in lines:
    if line.strip() == '':
        print(answers)
        print(len(answers))
        sum += len(answers)
        answers = set()
    else:
        for char in line:
            answers.add(char)
    print(line)

print(answers)
print(len(answers))
sum += len(answers)
print(sum)
