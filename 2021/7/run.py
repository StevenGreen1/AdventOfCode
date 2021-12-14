import os, sys

filename = "input.txt"

pos = []

with open(filename) as file:
    lines = file.readlines()
    pos = [int(item) for item in lines[0].split(',')]

pos_dict = {}

for item in pos:
    if item in pos_dict:
        pos_dict[item] += 1
    else:
        pos_dict[item] = 1

print(sorted(pos_dict))

min_fuel = 100000000

for index in range(min(pos_dict), max(pos_dict)):
    fuel = 0
    for item in pos_dict:
        fuel += pos_dict[item] * abs(item - index)
    min_fuel = min(fuel, min_fuel)
    if fuel == min_fuel:
        print("Position {} Fuel {}".format(index, fuel))
