#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    values = []
    for line in inputs:
        values.append(list(line))
    lows = []
    heights = []

    for n in range(0,len(values)):
        temp = []
        for m in range(0,len(values[0])):
            temp.append(0)
        heights.append(temp)
    y = len(values)
    x = len (values[0])
    for i in range(0,y):
        for j in range(0,x):
            #corners
            if i == 0 and j == 0:
                if values[i][j] < values [i+1][j] and values[i][j] < values [i][j+1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif i == 0 and j == (x-1):
                if values[i][j] < values [i+1][j] and values[i][j] < values [i][j-1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif i == y-1 and j == 0:
                if values[i][j] < values [i-1][j] and values[i][j] < values [i][j+1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif i == (y-1) and j == (x-1):
                if values[i][j] < values [i-1][j] and values[i][j] < values [i][j-1]:
                    heights[i][j] = int(values[i][j]) + 1
            # sides
            elif i == 0:
                if values[i][j] < values [i+1][j] and values[i][j] < values [i][j+1] and values[i][j] < values[i][j-1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif j == 0:
                if values[i][j] < values [i+1][j] and values[i][j] < values [i-1][j] and values[i][j] < values[i][j+1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif i == y-1:
                if values[i][j] < values [i-1][j] and values[i][j] < values [i][j-1] and values[i][j] < values[i][j+1]:
                    heights[i][j] = int(values[i][j]) + 1
            elif j == x-1:
                if values[i][j] < values [i-1][j] and values[i][j] < values [i+1][j] and values[i][j] < values[i][j-1]:
                    heights[i][j] = int(values[i][j]) + 1
            else:
                if values[i][j] < values [i][j-1] and values[i][j] < values [i][j+1] and values[i][j] < values[i-1][j] and values[i][j] < values[i+1][j]:
                    heights[i][j] = int(values[i][j]) + 1
    s = 0
    c=0
    for h in heights:
        print(h)
        s += sum(h)
        for r in h:
            if r != 0:
                c+=1
    print (s,c)
