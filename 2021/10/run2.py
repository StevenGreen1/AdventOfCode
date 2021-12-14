import os, sys, copy, math

filename = "input2.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print(lines)

def delete_from_string(string, idx):
    # Remove charactes from index 5 to 10
    if len(string) > idx :
        string = string[0: idx:] + string[idx + 1::]
    return string

open_chars  = ["[", "{", "<", "("]
close_chars = ["]", "}", ">", ")"]

def find_and_remove(line, isBroken):
    new_line = ""
    for idx, char in enumerate(line):
        if char in close_chars:
            if line[idx - 1] not in open_chars:
                isBroken = True
            elif close_chars.index(char) != open_chars.index(line[idx - 1]):
                isBroken = True

            if isBroken:
                return line, True, "NotDone"
            #print("Removing {} and {} from {}".format(line[idx], line[idx - 1], line))
            line = delete_from_string(line, idx)
            line = delete_from_string(line, idx - 1)
            return line, False, "NotDone"

    # Not broken just done
    return line, True, "Done"

fails = {}
for char in close_chars:
    fails[char] = 0

def score(line):
    score = 0
    for idx in range(len(line)-1, -1, -1):
        char = line[idx]
        score *= 5
        if char == "(":
            score += 1
        elif char == "[":
            score += 2
        elif char == "{":
            score += 3
        elif char == "<":
            score += 4
    return score

scores = []

for line in lines:
    orig_line = copy.deepcopy(line)
    broken = False
    while not broken:
#        print("Start line {}".format(line))
        line, broken, status = find_and_remove(line, broken)
#        print("End line {}".format(line))
    
        if status == "Done":
            mark = score(line)
            scores.append(mark)
#            print("Valid Line {}, Score {}".format(orig_line, mark))
            break
        
        if broken:
            for char in line:
                if char in close_chars:
                    #print(char)
                    fails[char] += 1
                    break
#            print("Invalid Lines {}".format(orig_line))

count = 0
for item in fails:
    if item == ")":
        count += 3 * fails[item]
    elif item == "]":
        count += 57 * fails[item]
    elif item == "}":
        count += 1197 * fails[item]
    elif item == ">":
        count += 25137 * fails[item]
print(count)

scores = sorted(scores)
print(scores)
print((len(scores)-1)/2)
print(scores[int((len(scores)-1)/2)])

for idx, val in enumerate(scores):
    print("{} {}".format(idx,val))
