import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

start = []
end = []

span = 1000
grid = [[0 for i in range(span)] for j in range(span)]

def print_grid(local_grid):
    print('')
    for item in local_grid:
        print(item)

for line in lines:
    points = line.split(' -> ')
    start.append([int(item) for item in points[0].split(',')])
    end.append([int(item) for item in points[1].split(',')])

for index in range(len(start)):
    s = start[index]
    e = end[index]
    if s[0] == e[0]:
        for val in range(min(s[1],e[1]), max(s[1],e[1]) + 1):
            grid[s[0]][val] += 1
    elif s[1] == e[1]:
        for val in range(min(s[0],e[0]), max(s[0], e[0]) + 1):
            grid[val][s[1]] += 1

count = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] > 1:
            count += 1

print_grid(grid)
# 2301 too low
print(count)
