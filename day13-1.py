#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

COUNT = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    dots = []
    fold = []
    for line in inputs:
        if line.startswith('f'):
            lin = line.split(' ')
            fold.append(lin[-1].split('='))
        else:
            dots.append(line)
    #print (dots)
    print (fold)
    grid = []
    xs = []
    ys = []
    for linee in dots[:-1]:
        line = linee.split(',')
        xs.append(int(line[0]))
        ys.append(int(line[1]))

    for i in range (0,max(ys)+1):
        temp = []
        for j in range (0, max(xs)+1):
            temp.append('')
        grid.append(temp)
    #for line in grid:
        #print (line)
    for i in range(0,len(dots)-1):
        grid[ys[i]][xs[i]] = '#'
    count=0
    for line in grid:
        print (line)
        for char in line:
            if char == '#':
                count += 1


    print(count)
    # fold along y = 7

    for f in folds:
        if
    f_v = int(7)
    x_v = 655
    for i in range(0,len(dots)-1):
        if xs[i] > x_v:
            new_x = x_v - (xs[i] - x_v)
            if grid[ys[i]][int(new_x)] != '#':
                grid[ys[i]][int(new_x)] = '#'

    count=0
    for line in grid:
        for char in line[0:x_v]:
            if char == '#':
                count += 1
    print(count)

    count = 0
    new_grid = []
    for line in grid:
        new_grid.append(line[0:x_v])
    for line in new_grid:
        #print (line)
        for char in  line:
            if char == '#': count +=1
    print(count)
