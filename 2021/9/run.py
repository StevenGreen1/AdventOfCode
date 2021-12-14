import os, sys

filename = "input.txt"

grid = []

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)

print(grid)

def isMin(grid, row, col):
    if row - 1 >= 0:
        if grid[row][col] >= grid[row - 1][col]:
            return False
    if row + 1 < len(grid):
        if grid[row][col] >= grid[row + 1][col]:
            return False
    if col - 1 >= 0:
        if grid[row][col] >= grid[row][col - 1]:
            return False
    if col + 1 < len(grid[0]):
        if grid[row][col] >= grid[row][col + 1]:
            return False
    return True

count = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if isMin(grid, row, col):
            count += (grid[row][col] + 1)
            print("Minimum Row {} Col {} Value {}".format(row,col,grid[row][col]))
print(count)
