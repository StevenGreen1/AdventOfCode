import os, sys, math

#filename = "input_test.txt"
filename = "input_final.txt"

with open(filename) as file:
    lines = file.readlines()

num = 99999999999999
while num > 9999999999999:
    num -= 1
    number = str(num)
    index = 0
    w = 0
    x = 0
    y = 0
    z = 0
    skip = False
    for i in number:
        if i == "0":
            skip = True

    if skip:
        continue

    print("Current Number {}".format(num), end='\r', flush=True)
    for line in lines:
        line = line.strip()
        split = line.split()
    
#        print(line)
#        print("Start - {} {} {} {}".format(w,x,y,z))
        if split[0] == "inp":
            w = number[index]
            index += 1
        else:
            inp1 = w if split[1] == "w" else x if split[1] == "x" else y if split[1] == "y" else z
            inp2 = w if split[1] == "w" else x if split[1] == "x" else y if split[1] == "y" else z
    
            if split[0] == "add":
                inp1 = inp1 + inp2
            elif split[0] == "mul":
                inp1 = inp1 * inp2
            elif split[0] == "div":
                if inp2 == 0:
                    skip = True
                    break
                inp1 = math.floor(inp1 / inp2)
            elif split[0] == "mod":
                if inp1 < 0 or inp2 <= 0:
                    skip = True
                    break
                inp1 = inp1 % inp2
            elif split[0] == "eql":
                inp1 = 1 if inp1 == inp2 else 0
    
#        print("End - {} {} {} {}".format(w,x,y,z))

#    print("Skip {}".format(skip))
    if skip:
        num -= (10 ** index)
        continue

    if z == 0:
        print(number)
        sys.exit()
