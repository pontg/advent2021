#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

MIN = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def dive(table, i, j, visited, count):
    global MIN
    count += int(table[i][j])
    visited.append((i,j))
    if i == len(table) -1 and j == len(table[0]) -1:
        if MIN == 0 or count < MIN:
            MIN == count
        print ("found exit")
        return count
    if i+1 < len(table) and (i+1,j) not in visited:
        dive( table, i+1, j, visited, count)
    if j+1 < len(table[0]) and (i,j+1) not in visited:
        dive( table, i, j+1, visited, count)
    if i > 0 and (i-1,j) not in visited:
        dive( table, i-1, j, visited, count)
    if j > 0 and (i, j-1) not in visited:
        dive( table, i, j-1, visited, count)
if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    table = []
    for i in inputs:
        temp = []
        for j in i:
            temp.append(j)
        table.append(temp)
    visited = [(0,0)]
    count = 0
    print( len(table), len(table[0]))
    dive(table, 0, 0, visited, count)
    print (MIN)
