import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

n_options = len(lines[0])
count = [0] * n_options
max_count = len(lines)
print(max_count)

for line in lines:
    for i in range(n_options):
        if line[i] == '1':
            count[i] += 1

print(count)

gamma = ''
epsilon = ''
for item in range(len(count)):
    if count[item] > 500:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma, int(gamma, 2))
print(epsilon, int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))
