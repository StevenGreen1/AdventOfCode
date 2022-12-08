import os, sys
from collections import Counter
import numpy as np

#filename = "input_test.txt"
filename = "input_final.txt"

size = 1
if 'final' in filename:
    size = 100
else:
    size = 10

grid = np.zeros((size, size))

with open(filename) as file:
    lines = file.readlines()
    for line_idx, line in enumerate(lines):
        line = line.strip()
        for char_idx, char in enumerate(line):
            grid[line_idx, char_idx] = int(char)

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.visited = False
        self.start_dist = 1e100
        self.previous_node = None

    def __str__(self):
        return "x {}, y, {}, value {}, visited {}, start_dist {}, previous node set {}".format(self.x, self.y, self.value,
                self.visited, self.start_dist,"True" if self.previous_node != None else "False")

def getNode(nodes, x, y):
    for node in nodes:
        if node.x == x and node.y == y:
            return node
    return None

def dijystra(grid):
    source = Node(0,0,0)
    source.start_dist = 0

    nodes = []

    for (x,y), value in np.ndenumerate(grid):
        node = Node(x,y,value)
        if x == 0 and y == 0:
            node.start_dist = 0
        nodes.append(node)

    while len(nodes) > 0:
        nodes = sorted(nodes, key=lambda x: x.start_dist, reverse=True)
        current_node = nodes.pop()
        #print('Current Node')
        #print(current_node)

        for nei_x, nei_y in [(1,0), (-1,0), (0,1), (0,-1)]:
            if current_node.x + nei_x < size and current_node.x + nei_x >= 0 and current_node.y + nei_y < size and current_node.y + nei_y >= 0:
                neighbour = getNode(nodes, current_node.x + nei_x, current_node.y + nei_y)
                if neighbour is None:
                    continue
                this_distance = current_node.start_dist + neighbour.value
                if this_distance < neighbour.start_dist:
                    neighbour.start_dist = this_distance
                    neighbour.previous_node = current_node

        if current_node.x == (size-1) and current_node.y == (size-1):
            print(current_node)

dijystra(grid)

#1  function Dijkstra(Graph, source):
# 2
# 3      create vertex set Q
# 4
# 5      for each vertex v in Graph:
# 6          dist[v] b INFINITY
# 7          prev[v] b UNDEFINED
# 8          add v to Q
# 9      dist[source] b 0
#10
#11      while Q is not empty:
#12          u b vertex in Q with min dist[u]
#13
#14          remove u from Q
#15
#16          for each neighbor v of u still in Q:
#17              alt b dist[u] + length(u, v)
#18              if alt < dist[v]:
#19                  dist[v] b alt
#20                  prev[v] b u
#21
#22      return dist[], prev[]
