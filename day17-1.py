#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict
from math import prod


# x=240..292, y=-90..-57
#TARGET_X_RANGE = (20,30)
#TARGET_Y_RANGE = (-10,-5)
TARGET_X_RANGE = (240,292)
TARGET_Y_RANGE = (-90,-57)
COUNT = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def trick_shot(x,y, vel_x, vel_y):
    global COUNT
    banco = False
    miss = False
    max_y = 0
    while not (banco or miss) :
        x += vel_x
        y += vel_y
        if y > max_y:
            max_y = y
        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        vel_y -= 1
        if ( x >= TARGET_X_RANGE[0] and
                x <= TARGET_X_RANGE[1] and
                y >= TARGET_Y_RANGE[0] and
                y <= TARGET_Y_RANGE[1]):
            banco = True
            COUNT += 1
        if ( x > TARGET_X_RANGE[1] or
                y < TARGET_Y_RANGE[0]):
            miss = True
    return (banco,x,y,max_y)

if __name__ == '__main__':
    max_y = 0
    for i in range(0, 600):
        for j in range (-200,200):
            pos = (0,0)
            catch,_, _,temp_y = trick_shot(pos[0],pos[1], i,j)
            if catch and temp_y > max_y:
                max_y = temp_y
    print (max_y)
    print (COUNT)
