import os, sys, math
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import heapq

filename = "input_test.txt"
#filename = "input_final.txt"

size = 1
if 'final' in filename:
    size = 100
else:
    size = 10

scale = 5

grid = np.zeros((size*5, size*5))

with open(filename) as file:
    lines = file.readlines()
    for line_idx, line in enumerate(lines):
        line = line.strip()
        for char_idx, char in enumerate(line):
            for i in range(5):
                for j in range(5):
                    x = line_idx + i * size
                    y = char_idx + j * size
                    total = i + j
                    val = int(char) + total if int(char) + total < 10 else int(char) + total - 9
                    grid[x, y] = val

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.start_dist = 1e100
        self.dist_to_go = 2*size*scale - 2 - x - y
        self.previous_node = None

    def __str__(self):
        return "x {}, y, {}, value {}, start_dist {}, distance to go {}".format(self.x, self.y, self.value, self.start_dist, self.dist_to_go)

    def __lt__(self, other):
        return self.start_dist + self.dist_to_go < other.start_dist + other.dist_to_go

def getNode(nodes, x, y):
    for node in nodes:
        if node.x == x and node.y == y:
            return node
    return None

def dijystra(grid):
    nodes = []

    for (x,y), value in np.ndenumerate(grid):
        node = Node(x,y,value)
        if x == 0 and y == 0:
            node.start_dist = 0
        nodes.append(node)

    X1 = []
    X2 = []
    Y1 = []
    Y2 = []

    heapq.heapify(nodes)

    while len(nodes) > 0:
        heapq.heapify(nodes)
        current_node = heapq.heappop(nodes)

        if len(nodes) % 100 == 0:
            print(current_node)

        if current_node.previous_node != None:
            X1.append(current_node.previous_node.x)
            X2.append(current_node.x)
            Y1.append(current_node.previous_node.y)
            Y2.append(current_node.y)

            plt.plot([current_node.previous_node.x, current_node.x], [current_node.previous_node.y, current_node.y], marker='o')
            plt.pause(0.001)

        for nei_x, nei_y in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbour = getNode(nodes, current_node.x + nei_x, current_node.y + nei_y)
            if neighbour is None:
                continue
            this_distance = current_node.start_dist + neighbour.value
            if this_distance < neighbour.start_dist:
                neighbour.start_dist = this_distance
                neighbour.previous_node = current_node

        if current_node.x == (size*scale-1) and current_node.y == (size*scale-1):
            print(current_node)
            return

dijystra(grid)
plt.show()

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
