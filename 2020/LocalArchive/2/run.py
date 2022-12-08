import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

valid = 0
for line in lines:
    minN = int(line.split('-')[0])
    maxN = int(line.split('-')[1].split()[0])
    let = line.split(':')[0].split()[1]
    password = line.split(':')[1]
    print(line)
    print("{} {} {} {}".format(minN, maxN, let, password))

    if int(password[minN] == let) + int(password[maxN] == let) == 1:
        print(password[minN])
        print(password[maxN])
        valid += 1
        print('valid')

#    count = 0
#    for i in password:
#        if i == let:
#            count += 1
#    if count >= minN and count <= maxN:
#        print('valid')
#        valid += 1

print(valid)
