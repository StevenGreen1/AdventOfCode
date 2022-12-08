import os, sys, re, copy, math
import numpy as np

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

estimated_time = int(lines[0])
busses = [int(x) for x in lines[1].split(',') if x != "x"]

print("Estimated time {}".format(estimated_time))
print("Busses {}".format(busses))

min_bus = 0
min_time = 1e10
for bus in busses:
    time = bus - (estimated_time % bus)
    if time < min_time:
        min_time = time
        min_bus = bus

print("Min Bus {}, Wait Time {}, Multp {}".format(min_bus, min_time, min_bus * min_time))
