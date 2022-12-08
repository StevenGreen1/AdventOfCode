import os, sys, math, copy
import numpy as np
import matplotlib.pyplot as plt

#Player 1 starting position: 6
#Player 2 starting position: 7

p1_place = 6
p2_place = 7

p1_win = 0
p2_win = 0

max_score = 21

def roll_p1(p1_scores_arg, p1_place_arg, p2_scores_arg, p2_place_arg, mul_arg):
#    print("P1 Roll")
    global p1_win, p2_win
    p1_rolls = [3, 4, 5, 6, 7, 8, 9]
    multip = [1, 3, 6, 7, 6, 3, 1]
    for idx, roll in enumerate(p1_rolls):
        p1_scores = copy.deepcopy(p1_scores_arg)
        p2_scores = copy.deepcopy(p2_scores_arg)
        p1_place = copy.deepcopy(p1_place_arg)
        p2_place = copy.deepcopy(p2_place_arg)
        mul = copy.deepcopy(mul_arg)
        mul *= multip[idx]
        p1_place += roll
        p1_place = (p1_place % 10)
        if p1_place == 0:
            p1_place = 10
        p1_scores.append(p1_place)
        if sum(p1_scores) >= max_score:
            p1_win += mul
            print("{} vs {}".format(p1_win, p2_win), end='\r', flush=True)
#            print("P1 Win {} vs {}".format(p1_scores, p2_scores))
        else:
            roll_p2(p1_scores, p1_place, p2_scores, p2_place, mul)

def roll_p2(p1_scores_arg, p1_place_arg, p2_scores_arg, p2_place_arg, mul_arg):
#    print("P2 Roll")
    global p2_win
    p2_rolls = [3, 4, 5, 6, 7, 8, 9]
    multip = [1, 3, 6, 7, 6, 3, 1]
    for idx, roll in enumerate(p2_rolls):
        p1_scores = copy.deepcopy(p1_scores_arg)
        p2_scores = copy.deepcopy(p2_scores_arg)
        p1_place = copy.deepcopy(p1_place_arg)
        p2_place = copy.deepcopy(p2_place_arg)
        mul = copy.deepcopy(mul_arg)
        mul *= multip[idx]
        p2_place += roll
        p2_place = (p2_place % 10) 
        if p2_place == 0:
            p2_place = 10
        p2_scores.append(p2_place)
        if sum(p2_scores) >= max_score:
            p2_win += mul
            print("{} vs {}".format(p1_win, p2_win), end='\r', flush=True)
#            print("P2 Win {} vs {}".format(p2_scores, p1_scores))
        else:
            roll_p1(p1_scores, p1_place, p2_scores, p2_place, mul)

roll_p1([], p1_place, [], p2_place, 1)

print("P1 W {}, P2 W {}".format(p1_win, p2_win))
