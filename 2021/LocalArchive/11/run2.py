import os, sys, copy
import numpy as np

filename = "input2.txt"

grid = []

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)

#grid = np.array(grid)
#print(grid)
#new_grid = grid
#new_grid[new_grid<8] = 0
#print(new_grid)
#conv = np.array([[1,1,1],[1,0,1],[1,1,1]])

adjacent = [[1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1], [0,1]]

def print_grid(grid):
    for row in grid:
        print(row)

def take_step(grid, flashes):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1
    return flash(grid)

flashes = 0

# Just perform the flash part, not the other incrementing
def flash(grid):
    flashes = 0
    new_grid = copy.deepcopy(grid)
    keep_going = True
    while keep_going:
        keep_going = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if new_grid[row][col] > 9:
                    flashes += 1
#                    print_grid(new_grid)
                    keep_going = True
                    new_grid[row][col] = 0
                    for adj_row, adj_col in adjacent:
                        if row + adj_row >= 0 and row + adj_row < len(grid) and col + adj_col >= 0 and col + adj_col < len(grid[0]):
                            if new_grid[row+adj_row][col+adj_col] != 0:
                                new_grid[row+adj_row][col+adj_col] += 1
    return new_grid, flashes

for step in range(1, 10000):
#    print('Step {}'.format(step))
#    print_grid(grid)
    grid, new_flashes = take_step(grid, flashes)
    flashes += new_flashes
    step_flashes = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                step_flashes += 1
    if step_flashes == 100:
        print("Step {}".format(step))
        break

#    print('')
#    print_grid(grid)
print(flashes)
