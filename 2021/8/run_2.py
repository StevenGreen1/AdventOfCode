import os, sys, copy

filename = "input.txt"

targets = []
digits = []

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        split = line.split('|')
        targets.append(split[1].split())
        digits.append(sorted(split[0].split(), key=len))

# 1 len == 2
# 4 len == 4
# 7 len == 3
# 8 len == 8

count = {1:0, 4:0, 7:0, 8:0}

def decode(digits, targets):
    print("Decode Digits {} Targets {}".format(digits, targets))
    code = {}

    # Sort each digit by alphabetical value
    sorted_digits = []
    for digit in digits:
        sorted_digits.append(sorted(digit))

    for digit in sorted_digits:
        print("Digit {}".format(digit))

        if len(digit) == 2:
            code[1] = digit
        elif len(digit) == 3:
            code[7] = digit
        elif len(digit) == 4:
            code[4] = digit
        elif len(digit) == 5:
            is2 = True
            for item in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
                if item not in digit:
                    # Make new work by adding letter and if in list skip as can't be 2
                    new_digit = copy.deepcopy(digit)
                    new_digit.append(item)
                    new_digit = "".join(sorted(new_digit))
                    for digit2 in sorted_digits:
                        lookup = "".join(digit2)
                        if new_digit == lookup:
                            is2 = False

            if is2:
                print("{} Is 2".format(digit))
                code[2] = digit
                continue

            is3 = True
            for val in code[1]:
                if val not in digit:
                    is3 = False
            if is3:
                print("{} Is 3".format(digit))
                code[3] = digit
            else:
                print("{} Is 5".format(digit))
                code[5] = digit
        elif len(digit) == 6:
            is6 = True
            is0 = True
            if code[1][0] in digit and code[1][1] in digit:
                is6 = False
            if is6:
                print("{} Is 6".format(digit))
                code[6] = digit
                continue

            if code[4][0] in digit and code[4][1] in digit and code[4][2] in digit and code[4][3] in digit:
                is0 = False
            if is0:
                print("{} Is 9".format(digit))
                code[0] = digit
            else:
                print("{} Is 0".format(digit))
                code[9] = digit
        elif len(digit) == 7:
            code[8] = digit

    decoder = {}

    for item in code:
        decoder[item] = "".join(code[item])

    string = ""
    for target in targets:
        print("Target {}".format(target))
        target = "".join(sorted(target))
        for item in decoder:
            if decoder[item] == target:
                string += str(item)
                print("Target {} = {}".format(target, item))
    return int(string)

count = 0
for index in range(len(targets)):
    count += decode(digits[index], targets[index])

print(count)
