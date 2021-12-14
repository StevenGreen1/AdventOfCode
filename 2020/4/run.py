import os, sys

filename = "input.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)
data = { "byr" : '',
        "iyr" : '',
        "eyr" : '',
        "hgt" : '',
        "hcl" : '',
        "ecl" : '',
        "pid" : '',
        "cid" : ''
        }


def wipe(dictionary):
    for key in dictionary:
        dictionary[key] = ''

def check(value, length, min_val, max_val):
    if len(value) != length:
        return False
    if int(value) < min_val:
        return False
    if int(value) > max_val:
        return False
    return True

def process(dictionary):
    targets = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for target in targets:
        if dictionary[target] == '':
            print('invalid')
            return 0

    if not check(dictionary["byr"], 4, 1920, 2002):
        return 0

    if not check(dictionary["iyr"], 4, 2010, 2020):
        return 0

    if not check(dictionary["eyr"], 4, 2020, 2030):
        return 0

    height = dictionary["hgt"]
    value = height[:-2]
    unit = height[-2:]

    if unit == 'cm':
        value = int(value)
        if value < 150 or value > 193:
            return 0
    elif unit == 'in':
        value = int(value)
        if value < 59 or value > 76:
            return 0
    else:
        return 0

    if dictionary["hcl"][0] != "#":
        return 0

    if len(dictionary["hcl"][1:]) != 6:
        return 0
    else:
        for i in dictionary["hcl"][1:]:
            if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"] :
                return 0

    if len(dictionary["pid"]) != 9:
        return 0

    string = "amb blu brn gry grn hzl oth"
    haircols = string.split(" ")
    if dictionary["ecl"] not in haircols:
        return 0
    print(unit)

    print('valid')
    return 1

count  = 0
for line in lines:
    if line.strip() == '':
        count += process(data)
        wipe(data)
    else:
        for item in line.split():
            data[item.split(':')[0]] = item.split(':')[1]
count += process(data)
print(count)
