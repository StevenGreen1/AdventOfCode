import os, sys, re, copy

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []

for index, line in enumerate(lines):
    numbers.append(int(line))

numbers.append(0)
numbers.append(max(numbers) + 3)
numbers = sorted(numbers)
print(numbers)

def iterate(initial_list, min_index = 1):
    local_count = 1
    # Have to keep 0 and last element
    for index in range(min_index, len(initial_list) - 1):
        if initial_list[index + 1] - initial_list[index - 1] < 4:
            next_list = copy.deepcopy(initial_list)
            next_list.remove(initial_list[index])
#            print(next_list)
            local_count += iterate(next_list, index)
    return local_count

numbers_list = []
sub_list = []

for index in range(1,len(numbers)):
    sub_list.append(numbers[index - 1])
    if numbers[index] - numbers[index - 1] == 3:
        numbers_list.append(sub_list)
        sub_list = []

factor = 1
for sub_list in numbers_list:
    print(sub_list)
    factor = factor * iterate(sub_list)
    print(factor)
print(factor)

# Part One
def isValidList(initial_list):
    counter = {}
    for index in range(1,len(initial_list)):
        gap = initial_list[index] - initial_list[index - 1]

        if gap in counter:
            counter[gap] += 1
        else:
            counter[gap] = 1

    print(counter)
    print(counter[3] * counter[1])

#isValidList(numbers)
