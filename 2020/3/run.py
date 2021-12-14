import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

grid = []

conversion = {'.' : 0, '#' : 1}

valid = 0
for line in lines:
    characters = [conversion[char] for char in line]
    grid.append(characters)


stepX = 3
stepY = 1


def check(grid, stepX, stepY):
    x = 0
    y = 0
    count = 0
    while True:
        if len(grid) - 1 < y:
            break
        count += int(grid[y][x%31])
        x += stepX
        y += stepY
    return count

print(check(grid, 1, 1))
print(check(grid, 3, 1))
print(check(grid, 5, 1))
print(check(grid, 7, 1))
print(check(grid, 1, 2))

print(check(grid, 1, 1) * check(grid, 3, 1) * check(grid, 5, 1) * check(grid, 7, 1) * check(grid, 1, 2))
