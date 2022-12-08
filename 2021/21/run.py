import os, sys, math
import numpy as np
import matplotlib.pyplot as plt

#Player 1 starting position: 6
#Player 2 starting position: 7

p1_score = 0
p2_score = 0

p1_place = 6
p2_place = 7

p1_roll_start = 6
p1_roll_count = 0
p2_roll_start = 15
p2_roll_count = 0

max_score = 1000

while p2_score < max_score:
    p1_roll = p1_roll_start + 18 * p1_roll_count
    p1_roll_count += 1
    p1_place += p1_roll
    p1_place = (p1_place % 10)
    if p1_place == 0:
        p1_place = 10
    p1_score += p1_place
    print("P1 Score {}, Roll {}, Place {}".format(p1_score, p1_roll, p1_place))

    if p1_score >= max_score:
        break

    p2_roll = p2_roll_start + 18 * p2_roll_count
    p2_roll_count += 1
    p2_place += p2_roll
    p2_place = (p2_place % 10)
    if p2_place == 0:
        p2_place = 10
    p2_score += p2_place
    print("P2 Score {}, Roll {}, Place {}".format(p2_score, p2_roll, p2_place))

print("P1 Score {} P2 Score {}".format(p1_score, p2_score))
print(p1_roll_count + p2_roll_count)
print(min(p1_score, p2_score) * (p1_roll_count + p2_roll_count) * 3)
