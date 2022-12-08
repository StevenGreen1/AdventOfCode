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

def follow(grid, row, col):
    if isMin(grid, row, col):
        return row, col

    if row - 1 >= 0:
        if grid[row][col] > grid[row - 1][col]:
            return follow(grid, row - 1, col)
    if row + 1 < len(grid):
        if grid[row][col] > grid[row + 1][col]:
            return follow(grid, row + 1, col)
    if col - 1 >= 0:
        if grid[row][col] > grid[row][col - 1]:
            return follow(grid, row, col - 1)
    if col + 1 < len(grid[0]):
        if grid[row][col] > grid[row][col + 1]:
            return follow(grid, row, col + 1)
    print("Should not get here!")

basins = {}
sizes = []

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 9:
            continue

        end_row, end_col = follow(grid, row, col)

        if (end_row, end_col) in basins:
            basins[(end_row,end_col)] += 1
        else:
            basins[(end_row,end_col)] = 1

for (row, col) in basins:
    sizes.append(basins[(row,col)])

print(sorted(sizes))
print(sorted(sizes)[-3:])
answer = sorted(sizes)[-3:][0] * sorted(sizes)[-3:][1] * sorted(sizes)[-3:][2]
print(answer)
