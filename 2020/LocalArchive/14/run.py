import os, sys, re, copy, math
import numpy as np

filename = sys.argv[1]

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

data = {}
#"MemoryAddr" : [],
#         "Value" : []

mask = 0

for line in lines:
    if "mask" in line:
        mask = line.split()[2]
    else:
        value = line.split()[2]
        addr = 0

        m = re.search('mem\[(.+?)\]', line)
        if m:
            addr = int(m.group(1))
        else:
            print("Problem - {}".format(line))

        print("Mask {}".format(mask))
        print("Value {}".format(value))
        str_value = [x for x in str(bin(int(value)))]
        str_value = str_value[2:]
        for i in range(len(str_value), len(mask)):
            str_value.insert(0,'0')
        print("String value {}".format(str_value))

        for idx, mask_val in enumerate(mask):
            if mask_val == 'X':
                continue
            str_value[idx] = mask_val

        string = ''.join(str_value)
        value = int(string, 2)
        print("Value {}".format(value))
        print("String value {}".format(str_value))

        data[addr] = value

count = 0
for i in data:
    count += data[i]
print("Final count {}".format(count))
