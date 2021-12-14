import os, sys
from collections import Counter

#filename = "input_test.txt"
filename = "input_final.txt"

rules = {}
start = ""

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        elif '->' not in line:
            start = line
        else:
            rule = line.split('->')
            rules[rule[0].strip()] = rule[1].strip()

def apply(line, rules):
    new_line = ""
    for index in range(0, len(line) - 1):
        local_pair = line[index] + line[index + 1]
        if local_pair in rules:
            new_line += line[index] + rules[local_pair]
        else:
            new_line += line[index]
    new_line += line[-1]
    return new_line

print(start)
for step in range(1):
    start = apply(start, rules)
    print(start)
#    print("Length {} - {}".format(len(start),start))

counter = Counter(start)
print(counter)

