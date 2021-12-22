#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict

class state():

    def __init__(self, pos1, val1, pos2, val2):
        self.p1_position = pos1
        self.p1_score = val1
        self.p2_position = pos2
        self.p2_score = val2

    def __repr__(self):
        return "state: {} {} {} {}".format(self.p1_position, self.p1_score, self.p2_position, self.p2_score)

    def __str__(self):
        return "p1 position: {},p1 score: {},p2 position: {},p2 score: {}".format(self.p1_position, self.p1_score, self.p2_position, self.p2_score)

nanou_prob = {3:1, 4:3, 5:6,6:7, 7:6, 8:3, 9:1}


states = defaultdict(int)
game = state(7,0,3,0)
states[game] = 1

print(game)
count_p1_win = 0
count_p2_win = 0

round = 0
while len(states) > 0:
    round += 1
    newstates = {}
    for i in states:
        for j in nanou_prob:
            # player 1 odd numbers
            if round % 2 == 1:
                position = (i.p1_position + j - 1 ) %10 + 1
                score = i.p1_score + position
                if score >= 21:
                    count_p1_win += states[i] * nanou_prob[j]
                else:
                    newstate = state(position,score, i.p2_position, i.p2_score)
                    #print (newstate)
                    newstates[newstate] = states[i] * nanou_prob[j]
            # player 2 even numbers
            else:
                position = (i.p2_position + j - 1 ) %10 + 1
                score = i.p2_score + position
                if score >= 21:
                    count_p2_win += states[i] * nanou_prob[j]
                else:
                    newstate = state( i.p1_position, i.p1_score,position,score)
                    newstates[newstate] = states[i] * nanou_prob[j]
    states = newstates
print( max(count_p1_win, count_p2_win))
