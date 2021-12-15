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
            temp.append('.')
        grid.append(temp)
    for i in range(0,len(dots)-1):
        grid[ys[i]][xs[i]] = '#'
    count=0
    for line in grid:
        for char in line:
            if char == '#':
                count += 1


    print(count)

    for f in fold:
        for line in grid:
            for char in  line:
                if char == '#': count +=1
        f_v = int(f[1])
        new_grid = []
        if f[0] == 'x':
            for i in range(0,len(xs)):
                if xs[i] >= f_v and ys[i] < len(grid):
                    new_x = f_v - (xs[i] - f_v)
                    if new_x >= 0:
                        grid[ys[i]][new_x] = '#'
                        xs.append(new_x)
                        ys.append(ys[i])
            for line in grid:
                new_grid.append(line[0:f_v])
        else:
            for i in range(0,len(ys)):
                if ys[i] >= f_v  and xs[i] < len(grid[0]):
                    new_y = f_v - (ys[i] - f_v)
                    if new_y >= 0 :
                        grid[new_y][xs[i]] = '#'
                        xs.append(xs[i])
                        ys.append(new_y)
            new_grid = grid[0:f_v]
        grid = new_grid


    for line in grid:
        print(''.join(line))
        for char in  line:
            if char == '#': count +=1
    print(count)
