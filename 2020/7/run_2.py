import os, sys, re
from anytree import Node, RenderTree

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

colours = set()

matches = {}

for line in lines:
    line = line[:-1]
    split_one = line.split(' bags contain')
    matches[split_one[0]] = {}
    colours.add(split_one[0])

    for rule in split_one[1].split(','):
        rule = rule.replace('bags','')
        rule = rule.replace('bag','')
        rule = rule.strip()
        matches[split_one[0]][rule[len(rule.split(' ')[0])+1:]] = rule.split(' ')[0]

nodes = {}

def add_next_level(total, matches, parent, multiplier):
    for match in matches:
        if match != parent:
            continue
        for child in matches[parent]:
            if matches[parent][child] == 'no':
                return total
            level_total = int(matches[parent][child]) * multiplier

            key = "{}".format(parent)
            node = Node("{} {}".format(child,level_total), parent=nodes[key])
            nodes[child] = node

            total += level_total
            total = add_next_level(total, matches, child, level_total)
    return total


string = 'shiny gold'
#string = 'dotted chartreuse'
targets = {string}
target_multip = {string : 1}
shiny_gold = Node(string, parent=None)
nodes[string] = shiny_gold

total = 0
total = add_next_level(total, matches, string, 1)
print(total)

for pre, fill, node in RenderTree(shiny_gold):
    print("%s%s" % (pre, node.name))

