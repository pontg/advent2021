#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def evaluategrid( grids: List[ord]) -> int:
    bingo = 0
    bingo_grid = -1
    for grid_index in range(0,len(grids)):
        # check lines
        for line in grids[grid_index]:
            if '-1' not in line:
                bingo = int(sum_grid(grids[grid_index]))
                bingo_grid = grid_index
        # check columns
        for i in range(0,5):
            found = 0
            sum = 0
            for j in range(0,5):
                if int(grids[grid_index][j][i]) == -1:
                    found += 1
                else :
                    sum += int(grids[grid_index][j][i])
            if found == 0:
                bingo = sum
                bingo_grid = grid_index
    return bingo, bingo_grid

def sum_grid(grid):
    summ = 0
    for i in range(0,5):
        for j in range(0,5):
            if int(grid[i][j]) != -1: summ += int(grid[i][j])
    return summ

def draw ( grids, draws):

    results = []
    for m in range (0, len(grids)):
        temp_grid = []
        for l in range(0,5):
            temp_grid.append(['-1']*5)
        results.append(temp_grid)
    for draw in draws:
        for j in range(0,len(grids)):
            for i in range(0,5):
                #print (grids[j][i])
                for k in range(0,5):
                    #print(grids[j][i][k])
                    if grids[j][i][k] == draw:
                        results[j][i][k] = draw
        if evaluategrid(results)[0] != 0:
            print("BIIIIIIIIIIIIIINGO " + draw)
            print ((sum_grid(grids[evaluategrid(results)[1]]) - evaluategrid(results)[0])* int(draw))
            return draw
    return

if __name__ == '__main__':
    args = parse_args()
    bingo_file = open(args.path, 'r').read()[:-1]
    draws = bingo_file.split()[0]
    grids = []
    for i in bingo_file.split('\n\n')[1:]:
        output = []
        lines = i.split('\n')
        for i in lines:
            line = []
            for k in i.split(' '):
                if k != '' : line.append(k)
            output.append(line)
        grids.append(output)
        #grids.append(line.split())
    #print(grids)
    draw(grids, draws.split(','))
    #print(brute_force(report.split()))
