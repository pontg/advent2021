#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def draw_line(map, x1,y1,x2,y2):
    if ( x1 == x2):
        for i in range (min(y1,y2), max(y1,y2)+1):
            map[i][x1] += 1
    elif (y1 == y2):
        for i in range (min(x1,x2), max(x1,x2)+1):
            map[y1][i] += 1
    else:
        if x1 < x2 and y1 < y2:
            for i in range (0,x2-x1+1):
                map[y1+i][x1+i] += 1
        elif x1 > x2 and y1 < y2:
            for i in range (0,x1-x2+1):
                map[y1+i][x1-i] += 1
        elif x1 < x2 and y1 > y2:
            for i in range (0,x2-x1+1):
                map[y1-i][x1+i] += 1
        elif x1 > x2 and y1 > y2:
            for i in range (0,x1-x2+1):
                map[y1-i][x1-i] += 1
    return map

def pretty_print_map(map):
    for i in map:
        print (i)

def count_danger_points(map):
    count = 0
    for line in map:
        for column in line:
            if column > 1: count += 1
    return count

def draw_map(lines):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for line in lines:
        x1.append(int(line.split(',')[0]))
        y1.append(int(line.split(',')[1]))
        x2.append(int(line.split(',')[2]))
        y2.append(int(line.split(',')[3]))
    max_x = max(max(x1),max(x2))
    max_y = max(max(y1),max(y2))
    print(max_x,max_y)
    map = [[0 for i in range(0,max_x+1)]for i in range(0,max_y+1)]

    for i in range(0,len(x1)):
        draw_line(map,x1[i],y1[i],x2[i],y2[i])
    #pretty_print_map (map)
    print (count_danger_points(map))

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1]
    lines = inputs.replace(' -> ',',').split('\n')
    draw_map(lines)
