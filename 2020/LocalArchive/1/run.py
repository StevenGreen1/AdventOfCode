import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

for line in sorted(lines):
    for line2 in sorted(lines, reverse=True):
        for line3 in sorted(lines, reverse=True):
            if line + line2 + line3 == 2020:
                print("{} + {} + {} = 2020, {} * {} * {} = {}".format(line, line2, line3, line, line2, line3, line3*line*line2))
                sys.exit()

