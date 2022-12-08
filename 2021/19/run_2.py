import os, sys, math
import numpy as np
import matplotlib.pyplot as plt

#filename = "input_test.txt"
filename = "input_final.txt"
offsets = []

class Scanner:
    def __init__(self, number, signals):
        self.number = number
        self.signals = signals
        self.vectors = []
        self.lookup = {}
        self.vectorize()
        self.matrix = None
        self.offset = None
        self.skip = False

    def __str__(self):
        return "Scanner {} : {} \n {}".format(self.number, self.signals, self.vectors)

    def vectorize(self):
        for idx1 in range(len(self.signals)):
            for idx2 in range(idx1 + 1, len(self.signals)):
                signal1 = self.signals[idx1]
                signal2 = self.signals[idx2]
                vector = signal2 - signal1
                mag = np.sqrt(vector.dot(vector))
                self.lookup[mag] = (signal1, signal2)
                self.vectors.append(np.sqrt(vector.dot(vector)))

    def set_rotation(self, matrix):
        self.matrix = matrix

        new_signals = []
        for signal in self.signals:
            new_signals.append(np.matmul(matrix, signal))

        self.signals = new_signals

    def set_offset(self, offset):
        self.offset = offset
        offsets.append(offset)

        new_signals = []
        for signal in self.signals:
            new_signals.append(signal - offset)
        
        self.signals = new_signals

    def steal(self, other_scanner):
        for signal in other_scanner.signals:
            self.signals.append(signal)

        self.lookup = {}
        self.vectors = []
        self.vectorize()

        other_scanner.signals = []
        return other_scanner

    def merge(self, scanner2):
        common = list(set(self.vectors).intersection(scanner2.vectors))
        max_len_common = max(common)
        print("max_len_common {}".format(max_len_common))
    
        ref_pos_1 = self.lookup[max_len_common]
        ref_pos_2 = scanner2.lookup[max_len_common]
    
    #    print(np.outer(ref_pos_1[0], ref_pos_2[0]))
    #    print(rotation_matrices)
    
        flip = False
        used = False

        matrix = np.array([[1,0,0],[0,1,0],[0,0,1]])

        for rotation in rotation_matrices:
            new_pos0 = np.matmul(rotation, ref_pos_2[0])
            new_pos1 = np.matmul(rotation, ref_pos_2[1])
    
            ref1 = new_pos0 - ref_pos_1[0]
            ref2 = new_pos1 - ref_pos_1[1]
            ref3 = new_pos0 - ref_pos_1[1]
            ref4 = new_pos1 - ref_pos_1[0]

            if np.array_equal(ref1, ref2):
                matrix = rotation
                flip = False
                used = True
                break
            if np.array_equal(ref3, ref4):
                matrix = rotation
                flip = True
                used = True
                break

        if used == False:
            return

        if False: #used == False:
            print(ref_pos_1)
            print(ref_pos_2)

            fig = plt.figure()
            ax = fig.add_subplot(projection='3d')
            x = []
            y = []
            z = []
            for signal in scanner2.signals:
                x.append(signal[0])
                y.append(signal[1])
                z.append(signal[2])
            ax.scatter(x, y, z, label = 'Pre rotation, Signal 2')

            x = []
            y = []
            z = []
            for signal in self.signals:
                x.append(signal[0])
                y.append(signal[1])
                z.append(signal[2])
    
            ax.scatter(x, y, z, label = 'Signal 1')
            ax.legend()
            plt.show()

        if flip:
            ref_pos_2s = np.matmul(matrix, ref_pos_2[1])
            ref_pos_2e = np.matmul(matrix, ref_pos_2[0])
        else:
            ref_pos_2s = np.matmul(matrix, ref_pos_2[0])
            ref_pos_2e = np.matmul(matrix, ref_pos_2[1])
    
        offset = ref_pos_2e - ref_pos_1[1]
        scanner2.set_rotation(matrix)
        scanner2.set_offset(offset)
    #    x = []
    #    y = []
    #    z = []
    #    for signal in self.signals:
    #        x.append(signal[0])
    #        y.append(signal[1])
    #        z.append(signal[2])
    #
    #    ax.scatter(x, y, z, label = 'Signal 1')
    #
    #    x2 = []
    #    y2 = []
    #    z2 = []
    #
    #    for signal in scanner2.signals:
    #        x2.append(signal[0])
    #        y2.append(signal[1])
    #        z2.append(signal[2])
    #    
    #    ax.scatter(x2, y2, z2, label = 'Signal 2')
        scanner2 = self.steal(scanner2)
        return
    #    ax.legend()
    #    plt.show()

scanners = []

rotation_matrices = [
        np.array([[1,0,0],[0,1,0],[0,0,1]]),
        np.array([[1,0,0],[0,0,-1],[0,1,0]]),
        np.array([[1,0,0],[0,-1,0],[0,0,-1]]),
        np.array([[1,0,0],[0,0,1],[0,-1,0]]),

        np.array([[0,-1,0],[1,0,0],[0,0,1]]),
        np.array([[0,0,1],[1,0,0],[0,1,0]]),
        np.array([[0,1,0],[1,0,0],[0,0,-1]]),
        np.array([[0,0,-1],[1,0,0],[0,-1,0]]),

        np.array([[-1,0,0],[0,-1,0],[0,0,1]]),
        np.array([[-1,0,0],[0,0,-1],[0,-1,0]]),
        np.array([[-1,0,0],[0,1,0],[0,0,-1]]),
        np.array([[-1,0,0],[0,0,1],[0,1,0]]),

        np.array([[0,1,0],[-1,0,0],[0,0,1]]),
        np.array([[0,0,1],[-1,0,0],[0,-1,0]]),
        np.array([[0,-1,0],[-1,0,0],[0,0,-1]]),
        np.array([[0,0,-1],[-1,0,0],[0,1,0]]),

        np.array([[0,0,-1],[0,1,0],[1,0,0]]),
        np.array([[0,0,1],[0,-1,0],[1,0,0]]),
        np.array([[0,-1,0],[0,0,-1],[1,0,0]]),
        np.array([[0,1,0],[0,0,1],[1,0,0]]),

        np.array([[0,0,-1],[0,-1,0],[-1,0,0]]),
        np.array([[0,-1,0],[0,0,1],[-1,0,0]]),
        np.array([[0,0,1],[0,1,0],[-1,0,0]]),
        np.array([[0,1,0],[0,0,-1],[-1,0,0]]),
        ]

with open(filename) as file:
    lines = file.readlines()
    number = 0
    signals = []
    for line in lines:
        line = line.strip()
        if line == "":
            scanners.append(Scanner(number, signals))
            number = 0
            signals = []
        elif "scanner" in line:
            split = line.split()
            number = int(split[2])
        else:
            signals.append(np.array([int(x) for x in line.split(",")]))

    scanners.append(Scanner(number, signals))

def from_triange(number):
    return math.sqrt((2 * number) + 0.25) - 0.5

def iterate(scanners):
    new_scanners = scanners
    for idx1 in range(len(scanners)):
        for idx2 in range(idx1 + 1, len(scanners)):
            scanner1 = scanners[idx1]
            scanner2 = scanners[idx2]

            # List of vectors with same magnitude
            common = list(set(scanner1.vectors).intersection(scanner2.vectors))

            # Number of shared elements is len(common) + 1 as it takes two signals to make the first vector
            number_of_shared_signals = len(common) + 1
            print("Number of shared signals between {} and {} = {}".format(idx1, idx2, number_of_shared_signals))

            if number_of_shared_signals >= 12:
                scanner1.merge(scanner2)
                new_scanners.remove(scanner2)

                count = len(scanner1.signals)
                count2 = len(scanner2.signals)
                print("Count of merged set {}".format(count))
                print("Count of merged set {}".format(count2))
                return new_scanners


total = 0
shared = 0



def count(scanners):
    count = 0
    for scanner in scanners:
        if len(scanner.signals) > 0:
            count += 1

    print("Count {}".format(count))
    if count > 1:
        return True
    return False

while len(scanners) > 1:
    scanners = iterate(scanners)


count_list = []
for signal in scanners[0].signals:
    if (signal[0],signal[1],signal[2]) in count_list:
        continue
    count_list.append((signal[0],signal[1],signal[2]))
print(len(count_list))


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for idx, i in enumerate(scanners):
    x = []
    y = []
    z = []
    for signal in i.signals:
        x.append(signal[0])
        y.append(signal[1])
        z.append(signal[2])
    ax.scatter(x, y, z, label = 'Signal {}'.format(idx))

ax.legend()
plt.show()

print(offsets)

max_dist = 0
for i in range(len(offsets)):
    for j in range(i + 1, len(offsets)):
        distance = abs(offsets[i][0] - offsets[j][0]) + abs(offsets[i][1] - offsets[j][1]) + abs(offsets[i][2] - offsets[j][2])
        max_dist = max(distance, max_dist)
print(max_dist)
# 372 too low
# 422 high
