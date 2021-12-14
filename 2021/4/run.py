import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

call_numbers = [item for item in lines[0].split(',')]

print(call_numbers)

def print_grid(grid):
    print('')
    for line in grid:
        print(line)

def make_grids(lines):
    grids = []
    grid = 5 * [5 * [0]]
    row = 0
    for number in lines[2:]:
        if number == '':
#            print_grid(grid)
            grids.append(grid)
            grid = 5 * [5 * [0]]
            row = 0
            continue

        to_add = []
        for i in number.split():
            to_add.append([i, False])
        grid[row] = to_add
        row += 1

#    print_grid(grid)
    grids.append(grid)
    return grids

def add_and_check(grid, number):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col][0] == number:
                grid[row][col][1] = True
                break

    for row in range(len(grid)):
        if grid[row][0][1] == True and grid[row][1][1] == True and grid[row][2][1] == True and grid[row][3][1] == True and grid[row][4][1] == True:
            print('Got a row')
            return True

    for col in range(len(grid)):
        if grid[0][col][1] == True and grid[1][col][1] == True and grid[2][col][1] == True and grid[3][col][1] == True and grid[4][col][1] == True:
            print('Got a column')
            return True

    if grid[0][0][1] == True and grid[1][1][1] == True and grid[2][2][1] == True and grid[3][3][1] == True and grid[4][4][1] == True:
        print('Diagonal')
        return True
    if grid[0][4][1] == True and grid[1][3][1] == True and grid[2][2][1] == True and grid[3][1][1] == True and grid[4][0][1] == True:
        print('Reverse Diagonal')
        return True
    return False

grids = make_grids(lines)

for called in call_numbers:
    print("Calling {}".format(called))
    for grid in grids: #grids[:1]:
        if add_and_check(grid, called):
            print_grid(grid)

            marked = 0
            unmarked = 0
            for row in range(5):
                for col in range(5):
                    if grid[row][col][1] == True:
                        marked += int(grid[row][col][0])

                    else:
                        unmarked += int(grid[row][col][0])
            print(marked, unmarked)
            print(int(called) * unmarked)
            sys.exit()
