import os, sys, re

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

def lookup(matches, targets):
    to_add = []
    for item in matches:
        for target in targets:
            if target in matches[item]:
                to_add.append(item)
    for item in to_add:
        targets.add(item)
    return targets

targets = {'shiny gold'}
keep_going = True
i = 0

while i < 10:
    print(targets)
    print(len(targets))
    targets = lookup(matches, targets)
    i += 1

print(len(targets))
