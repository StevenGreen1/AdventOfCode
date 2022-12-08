import os, sys

filename = "input.txt"

targets = []
digits = []

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        split = line.split('|')
        targets.append(split[1].split())
        digits.append(split[0].split())
    lines = [line.strip() for line in lines]

# 1 len == 2
# 4 len == 4
# 7 len == 3
# 8 len == 8

count = {1:0, 4:0, 7:0, 8:0}

for local_digits in targets:
    for digit in sorted(local_digits,key=len):
        if len(digit) == 2:
            count[1] += 1
        elif len(digit) == 4:
            count[4] += 1
        elif len(digit) == 3:
            count[7] += 1
        elif len(digit) == 7:
            count[8] += 1

total = 0
for item in count:
    total += count[item]
print(count)
print(total)

