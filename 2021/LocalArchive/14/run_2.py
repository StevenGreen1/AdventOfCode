import os, sys
from collections import Counter
import numpy as np

#filename = "input_test.txt"
filename = "input_final.txt"

rules = {}
indices = {}
start = ""

with open(filename) as file:
    lines = file.readlines()
    counter = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        elif '->' not in line:
            start = line
        else:
            rule = line.split('->')
            rules[rule[0].strip()] = rule[1].strip()
            indices[rule[0].strip()] = counter
            counter += 1

print(rules)
print(indices)

size = len(rules)
steps = 40

def build_matrix(rules):
    matrix = np.zeros((size, size))
    for rule in rules:
        end0 = rule[0] + rules[rule]
        end1 = rules[rule] + rule[1]
        matrix[indices[end0], indices[rule]] = matrix[indices[end0], indices[rule]] + 1
        matrix[indices[end1], indices[rule]] = matrix[indices[end1], indices[rule]] + 1
    return matrix

matrix = build_matrix(rules)
if steps > 1:
    final_matrix = np.linalg.matrix_power(matrix, steps)
else:
    final_matrix = matrix

vector = np.zeros(size)
for i in range(len(start) - 1):
    vector[indices[start[i:i+2]]] += 1

print('Vector')
print(vector)
print('Matrix')
print(final_matrix)
print('Answer')
answer = final_matrix.dot(vector)
print(answer)

counter_dict = {}

for index in range(len(answer)):
    for j in indices:
        if index == indices[j]:
            letter = j[0]
            if letter in counter_dict:
                counter_dict[letter] += int(answer[index])
            else:
                counter_dict[letter] = int(answer[index])
            continue

counter_dict[start[-1]] += 1
print(counter_dict)
values = counter_dict.values()
print(max(values) - min(values))

