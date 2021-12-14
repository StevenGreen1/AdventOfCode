import os, sys, copy

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

o2_levels = copy.deepcopy(lines)
co2_levels = copy.deepcopy(lines)
key = 0

def nextCommonIndex(list, index, mostCommon = True):
    count = 0
    for item in list:
        if item[index] == '1':
            count += 1
    if count == len(list)/2:
        return '1' if mostCommon else '0'
    elif count > len(list)/2:
        return '1' if mostCommon else '0'
    return '0' if mostCommon else '1'

while len(o2_levels) > 1:
    print("\nIndex {}".format(key))
    print(o2_levels)
    nextCommonVal = nextCommonIndex(o2_levels, key,  True)
    print(nextCommonVal)
    o2_levels = [value for value in o2_levels if value[key] == nextCommonVal]
    key += 1

key = 0
while len(co2_levels) > 1:
#    print("\nIndex {}".format(key))
#    print(co2_indices[key])
#    print(co2_levels)
    nextCommonVal = nextCommonIndex(co2_levels, key, False)
    co2_levels = [value for value in co2_levels if value[key] == nextCommonVal]
#    print(co2_levels)
    key += 1

print(o2_levels)
print(co2_levels)

# 3366884 wrong
# 3625216 too low
# 4568237 
#print(int(o2_levels[0], 2))    
print(int(o2_levels[0], 2) * int(co2_levels[0], 2))    
