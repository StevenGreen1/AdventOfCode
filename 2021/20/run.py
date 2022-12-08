import os, sys, math
import numpy as np
import matplotlib.pyplot as plt

#filename = "input_test.txt"
filename = "input_final.txt"

class GridPoint:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.next = None
        self.neighbours = {0 : None, 1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None}

    def __str__(self):
        return "{}, {} : Value {}".format(self.x, self.y, self.value)

    def calc_next(self, lookup):
        value = str(self.neighbours[0].value)
        value += str(self.neighbours[1].value)
        value += str(self.neighbours[2].value)
        value += str(self.neighbours[3].value)
        value += str(self.value)
        value += str(self.neighbours[4].value)
        value += str(self.neighbours[5].value)
        value += str(self.neighbours[6].value)
        value += str(self.neighbours[7].value)
        self.next = lookup[int(value, 2)]

    def set_next(self):
        if self.next != None:
            self.value = self.next
            self.next = None

with open(filename) as file:
    lines = file.readlines()

conversion = lines[0].strip()
lookup = {}

for idx, char in enumerate(conversion):
    if char == "#":
        lookup[idx] = 1
    else:
        lookup[idx] = 0

grid = []

for row, line in enumerate(lines[2:]):
    points = []
    for col, char in enumerate(line.strip()):
        value = 1 if char == "#" else 0
        points.append(GridPoint(value, col, row))
    grid.append(points)

def print_grid(grid):
    for line in grid:
        for val in line:
            print(val)

def count_grid(grid):
    count = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col].value == 1:
                count += 1
    print("Grid count is {}".format(count))

def increase_size(grid, count):
    new_pix = 0 if count % 2 == 0 else 1
    new_grid = []
    new_line = []
    for i in range(len(grid[0]) + 2):
        new_line.append(GridPoint(new_pix,i,0))
    new_grid.append(new_line)

    for row, line in enumerate(grid):
        new_line = line
        for item in line:
            item.x = item.x + 1
            item.y = item.y + 1
        new_line.insert(0, GridPoint(new_pix,0,row+1))
        new_line.append(GridPoint(new_pix,len(new_line),row+1))
        new_grid.append(new_line)

    new_line = []
    for i in range(len(grid[0])):
        new_line.append(GridPoint(new_pix,i,len(grid)+1))
    new_grid.append(new_line)
    print("Old grid size {} x {} -> New grid size {} x {}".format(len(grid), len(grid[0]), len(new_grid), len(new_grid[0])))
    return new_grid


def step(grid, lookup, count):
    print("Stepping X between 1 and {} and Y between 1 and {}".format(len(grid) - 2, len(grid[0]) - 2))
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            current = grid[row][col]
            current.neighbours[0] = grid[row-1][col-1]
            current.neighbours[1] = grid[row-1][col]
            current.neighbours[2] = grid[row-1][col+1]
            current.neighbours[3] = grid[row][col-1]
            current.neighbours[4] = grid[row][col+1]
            current.neighbours[5] = grid[row+1][col-1]
            current.neighbours[6] = grid[row+1][col]
            current.neighbours[7] = grid[row+1][col+1]
            current.calc_next(lookup)

    new_pix = 1 if count % 2 == 0 else 0

    for row in [0, len(grid)-1]:
        for col in range(len(grid[0])):
            current = grid[row][col]
            current.value = new_pix
    for row in range(1, len(grid) - 1):
        for col in [0, len(grid[0])-1]:
            current = grid[row][col]
            current.value = new_pix

    for line in grid:
        for item in line:
            item.set_next()

grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)
grid = increase_size(grid, 0)

count_grid(grid)

def plot_grid(grid):
    x = []
    y = []
    x2 = []
    y2 = []
    for i in grid:
        for item in i:
            if item.value == 1:
                x.append(item.x)
                y.append(-item.y)
            elif item.value == 0:
                x2.append(item.x)
                y2.append(-item.y)
    
    plt.plot(x, y, 'o', color='red');
    plt.plot(x2, y2, 'o', color='blue');
    plt.show()

print('Grid 1')
plot_grid(grid)
for i in range(2):
    grid = increase_size(grid, i)
    step(grid, lookup, i)
    print('Grid {}'.format(i+1))
    plot_grid(grid)

count_grid(grid)
#5296 too low
#5901 too high
#5884 
