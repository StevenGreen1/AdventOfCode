import os, sys, ast, math
from collections import Counter
import numpy as np

filename = "input_test.txt"
#filename = "input_final.txt"

numbers = []
with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        if line.strip() == "":
            break
        numbers.append(ast.literal_eval(line.strip()))

class Node:
    def __init__(self, values):
        self.left = None
        self.right = None
        self.parent = None
        self.value = 0

        if isinstance(values, list):
            if len(values) == 2:
                self.left = Node(values[0])
                self.left.parent = self
                self.right = Node(values[1])
                self.right.parent = self
            else:
                print("Problem")
        else:
            self.value = values

    def __str__(self):
        if self.left == None and self.right == None:
            return str(self.value)
        else:
            return "[{}, {}]".format(self.left, self.right)

    def __add__(self, o):
        addition = Node(0)
        addition.right = o
        addition.right.parent = addition
        addition.left = self
        addition.left.parent = addition
        return addition

def traverse(node, out, depth):
    if node.left == None and node.right == None:
        out.append((node,depth))
        return out
    else:
        out = traverse(node.left, out, depth + 1)
        out = traverse(node.right, out, depth + 1)
        return out

def reduce(node, depth):
    if node.left == None and node.right == None:
        if depth >= 5:
            print("Explode")
            left = node.parent.left.value
            right = node.parent.right.value

            parent_node = node.parent
            while parent_node.parent != None:
                parent_node = parent_node.parent
            nodes = []
            nodes = traverse(parent_node, nodes, 0)

            left_index = nodes.index((node,depth))
            right_index = left_index + 1

            if left_index - 1 >= 0:
                left_node = nodes[left_index - 1][0]
                left_node.value += left

            if right_index + 1 < len(nodes):
                right_node = nodes[right_index + 1][0]
                right_node.value += right

            node.parent.left = None
            node.parent.right = None
            node.parent = None
            return True

        if node.value >= 10:
            print("Split")
            split_val_min = math.floor(node.value / 2)
            split_val_max = math.ceil(node.value / 2)
            node.value = 0
            node.left = Node(split_val_min)
            node.right = Node(split_val_max)
            node.left.parent = node
            node.right.parent = node
            return True

        return False
    else:
        changed = reduce(node.left, depth + 1)
        if changed:
            return True
        return reduce(node.right, depth + 1)

parent = Node(numbers[0])
print(parent)

for number in numbers[1:]:
    parent = parent + Node(number)
    print("+ {}".format(Node(number)))
    print(parent)

    changed = True
    while changed == True:
        changed = reduce(parent, 0)
        print(parent)

    sys.exit()
#    parent2 = parent + [1,1]
#    print(parent2)

print(parent)

