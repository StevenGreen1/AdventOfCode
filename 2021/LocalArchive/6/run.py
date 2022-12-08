import os, sys

filename = "input.txt"

fishes = []

with open(filename) as file:
    lines = file.readlines()
    fishes = [int(item) for item in lines[0].split(',')]

fish_dict = {}

for item in fishes:
    if item in fish_dict:
        fish_dict[item] += 1
    else:
        fish_dict[item] = 1

print(fish_dict)

for day in range(256):
    next_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for level in fish_dict:
        if level == 0:
            next_dict[8] += fish_dict[level]
            next_dict[6] += fish_dict[level]
        else:
            next_dict[level - 1] += fish_dict[level]

    fish_dict = next_dict

print(fish_dict)

count = 0
for idx in fish_dict:
    count += fish_dict[idx]

print(count)

