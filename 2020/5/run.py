import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def nextRow(letter, minRow, maxRow):
    if letter == 'B':
        minRow = minRow + round((maxRow - minRow)/2)
    elif letter == 'F':
        maxRow = maxRow - round((maxRow - minRow)/2)
    return minRow, maxRow

def lastRow(letter, minRow, maxRow):
    if letter == 'F':
        return minRow
    else:
        return maxRow

column = { 'RRR' : 7,
        'RRL' : 6,
        'RLR' : 5,
        'RLL' : 4,
        'LRR' : 3,
        'LRL' : 2,
        'LLR' : 1,
        'LLL' : 0}

def process(line):
    minRow = 0
    maxRow = 127
    minRow, maxRow = nextRow(line[0], minRow, maxRow)
    minRow, maxRow = nextRow(line[1], minRow, maxRow)
    minRow, maxRow = nextRow(line[2], minRow, maxRow)
    minRow, maxRow = nextRow(line[3], minRow, maxRow)
    minRow, maxRow = nextRow(line[4], minRow, maxRow)
    minRow, maxRow = nextRow(line[5], minRow, maxRow)
    row = lastRow(line[6], minRow, maxRow)
    col = column[line[-3:]]
    print(line)
    print("{} {} {}".format(row, col, row * 8 + col))
    return row * 8 + col

target = 0
full_list = []
for line in lines:
#    if line[:7] != 'BBBBFBB':
#        continue
    target = max(process(line), target)
    full_list.append(process(line))

for i in range(0,989):
    if i not in full_list:
        print(i)

print(target)

