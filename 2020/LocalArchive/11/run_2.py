import os, sys, re, copy
import numpy as np

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

seating_plan =  []

for index, line in enumerate(lines):
    row = [char for char in line.strip()]
    seating_plan.append(row)

#Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:
#
#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
#If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
#Otherwise, the seat's state does not change.
#Floor (.) never changes; seats don't move, and nobody sits on the floor.

def count(plan, row, col):
    steps = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1, 1]]

    n_tag = 0
    n_empty = 0

    for step in steps:
        new_row = row
        new_col = col
        count_step = False

        while True:
            new_row += step[0]
            new_col += step[1]

            if new_row < 0 or new_row >= len(plan):
                break
            elif new_col < 0 or new_col >= len(plan[new_row]):
                break

            count_step = True

            value = plan[new_row][new_col]
            if value == '#':
                n_tag += 1
                break
            elif value == 'L':
                n_empty += 1
                break

    return n_tag, n_empty

initial_plan = seating_plan
changed = True

def print_plan(plan):
    for line in plan:
        print(" ".join(line))

print('Initial')
print_plan(initial_plan)
while changed:
    local_plan = copy.deepcopy(initial_plan)
#    print('Initial')
#    print_plan(initial_plan)

    for row in range(0, len(local_plan)):
        for col in range(0, len(local_plan[row])):
            if local_plan[row][col] == '.':
                continue
            n_tag, n_empty = count(initial_plan, row, col)

            if local_plan[row][col] == 'L' and n_tag == 0:
                local_plan[row][col] = '#'
            elif local_plan[row][col] == '#' and n_tag > 4:
                local_plan[row][col] = 'L'
    
    changed = True if local_plan != initial_plan else False
    print(changed)
    print('Final')
    print_plan(local_plan)
    initial_plan = local_plan

print_plan(initial_plan)

count = 0
for row in range(0, len(initial_plan)):
    for col in range(0, len(local_plan[row])):
        if initial_plan[row][col] == '#':
            count += 1
print(count)

# 137 too low
