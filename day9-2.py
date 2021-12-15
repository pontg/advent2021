#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests



def basin(table,visited,i,j,x,y,count):
    seen = False
    if i+1<y and int(table[i+1][j]) == (int(table[i][j]) + 1) and visited[i+1][j] == False:
        if int(table[i+1][j]) != 9:count = basin(table,visited,i+1,j,x,y,count)
        seen = True
    if j+1<x and int(table[i][j+1]) == (int(table[i][j]) + 1) and  visited[i][j+1]== False:
        if int(table[i][j+1]) != 9:count = basin(table,visited,i,j+1,x,y,count)
        seen = True
    if i>0 and int(table[i-1][j]) == (int(table[i][j]) + 1) and  visited[i-1][j]== False:
        if int(table[i-1][j]) != 9:
            count = basin(table,visited,i-1,j,x,y,count)
        seen = True
    if j>0 and int(table[i][j-1]) == (int(table[i][j]) + 1) and  visited[i][j-1] == False:
        if int(table[i][j-1]) != 9:
            count = basin(table,visited,i,j-1,x,y,count)
        seen = True
    visited[i][j] = True
    return count + int(seen)

def visit_basin_archive(table,visited,i,j,x,y):
    seen = False
    if i+1<y and int(table[i+1][j]) == (int(table[i][j]) + 1) and visited[i+1][j] == False:
        if int(table[i+1][j]) != 9:
            visit_basin(table,visited,i+1,j,x,y)
        seen = True
    if j+1<x and int(table[i][j+1]) == (int(table[i][j]) + 1) and  visited[i][j+1]== False:
        if int(table[i][j+1]) != 9:
            visit_basin(table,visited,i,j+1,x,y)
        seen = True
    if i>0 and int(table[i-1][j]) == (int(table[i][j]) + 1) and  visited[i-1][j]== False:
        if int(table[i-1][j]) != 9:
            visit_basin(table,visited,i-1,j,x,y)
        seen = True
    if j>0 and int(table[i][j-1]) == (int(table[i][j]) + 1) and  visited[i][j-1] == False:
        if int(table[i][j-1]) != 9:
            visit_basin(table,visited,i,j-1,x,y)
        seen = True
    visited[i][j] = True
    return count + int(seen)

def visit_basin(table,visited,i,j,x,y):
    seen = False
    if i+1<y and int(table[i+1][j]) >= (int(table[i][j]) + 1) and visited[i+1][j] == False:
        if int(table[i+1][j]) != 9:
            visit_basin(table,visited,i+1,j,x,y)
        seen = True
    if j+1<x and int(table[i][j+1]) >= (int(table[i][j]) + 1) and  visited[i][j+1]== False:
        if int(table[i][j+1]) != 9:
            visit_basin(table,visited,i,j+1,x,y)
        seen = True
    if i>0 and int(table[i-1][j]) >= (int(table[i][j]) + 1) and  visited[i-1][j]== False:
        if int(table[i-1][j]) != 9:
            visit_basin(table,visited,i-1,j,x,y)
        seen = True
    if j>0 and int(table[i][j-1]) >= (int(table[i][j]) + 1) and  visited[i][j-1] == False:
        if int(table[i][j-1]) != 9:
            visit_basin(table,visited,i,j-1,x,y)
        seen = True
    visited[i][j] = True
    return count + int(seen)

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
                if int(values[i][j]) < int(values[i+1][j]) and int(values[i][j]) < int(values [i][j+1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif i == 0 and j == (x-1):
                if int(values[i][j]) < int(values[i+1][j]) and int(values[i][j]) < int(values[i][j-1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif i == y-1 and j == 0:
                if int(values[i][j]) < int(values[i-1][j]) and int(values[i][j]) < int(values[i][j+1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif i == (y-1) and j == (x-1):
                if int(values[i][j]) < int(values [i-1][j]) and int(values[i][j]) < int(values [i][j-1]):
                    heights[i][j] = int(values[i][j]) + 1
            # sides
            elif i == 0:
                if int(values[i][j]) < int(values [i+1][j]) and int(values[i][j]) < int(values [i][j+1]) and int(values[i][j]) < int(values[i][j-1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif j == 0:
                if int(values[i][j]) < int(values [i+1][j]) and int(values[i][j]) < int(values[i-1][j]) and int(values[i][j]) < int(values[i][j+1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif i == y-1:
                if int(values[i][j]) < int(values [i-1][j]) and int(values[i][j]) < int(values [i][j-1]) and int(values[i][j]) < int(values[i][j+1]):
                    heights[i][j] = int(values[i][j]) + 1
            elif j == x-1:
                if int(values[i][j]) < int(values[i-1][j]) and int(values[i][j]) < int(values[i+1][j]) and int(values[i][j]) < int(values[i][j-1]):
                    heights[i][j] = int(values[i][j]) + 1
            else:
                if int(values[i][j]) < int(values[i][j-1]) and int(values[i][j]) < int(values[i][j+1]) and int(values[i][j]) < int(values[i-1][j]) and int(values[i][j]) < int(values[i+1][j]):
                    heights[i][j] = int(values[i][j]) + 1


    print(heights[2])
    basins = []
    for m in range(0,y):
        for n in range(0,x):
            #print("========================")
            count = 1
            if heights[m][n] != 0 and heights[m][n] != 10 :
                visited = []

                for u in range(0,len(values)):
                    temp = []
                    for u in range(0,len(values[0])):
                        temp.append(False)
                    visited.append(temp)
                visit_basin(values,visited,m,n,x,y)
                t = 0
                for g in visited:
                    #print(g)
                    for h in g:
                        t += int(h)
                basins.append(t)
    print (basins)
    basins.sort()

    print (len(basins))
    print(basins[-1]*basins[-2]*basins[-3])
