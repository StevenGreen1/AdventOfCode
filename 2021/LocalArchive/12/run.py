import os, sys, copy
import numpy as np

filename = "input_final.txt"

connections = {}

def add_connection(connections, start, end):
    if start in connections:
        connections[start].append(end)
    else:
        connections[start] = [end]

    if end in connections:
        connections[end].append(start)
    else:
        connections[end] = [start]

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        vals = line.strip().split('-')
        add_connection(connections, vals[0], vals[1])

def take_step(node, connections, current_path):
    paths = []
    for connection in connections[node]:
#        if node == 'end':
#            # If node is end stop and return valid paths
#            paths.append(current_path)
        if connection.islower() and connection in current_path:
            # Is node is lower case, meaning small cave, and current cave is in path, path not allowed
            continue
        else:
            next_path = current_path + '-' + connection
            if connection == 'end':
                paths.append(next_path)
            else:
                paths += take_step(connection, connections, next_path)
    return paths

check_paths = []
for connection in connections:
    if connection == 'start' or connection == 'end':
        continue
    if connection.islower():
        check_paths.append(connection)

print(connections)
print(check_paths)
paths = take_step('start', connections, 'start')

count = 0
for path in paths:
    path = path.replace('start-','')
    path = path.replace('-end','')
    for check in check_paths:
        if check in path:
            count += 1
            break

print(count)
#print(len(paths))
#print(paths)
