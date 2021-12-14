import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

answers = []
sum = 0
for line in lines:
    if line.strip() == '':
        inter = answers[0]
        for item in answers[1:]:
            inter = inter & item
            print("item : {}".format(item))
            print(inter)
        print(inter)
        print(len(inter))
        sum += len(inter)
        answers = []
    else:
        answer = set()
        for char in line:
            answer.add(char)
        answers.append(answer)
        print(answer)
    print(line)

inter = answers[0]
for item in answers[1:]:
    inter = inter.intersection(item)
print(inter)
print(len(inter))
sum += len(inter)
print(sum)
