#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def translate ( inp):
    if inp =="#":
        return str(1)
    if inp == ".":
        return str(0)

def get_number(grid,x,y,val):
    temp = ""
    if y > 0 and x > 0:
        temp += translate(grid[x-1][y-1])
    else:
        temp+= translate(val)
    if x > 0 :
        temp += translate(grid[x-1][y])
    else:
        temp+= translate(val)
    if x >0 and y < len(grid[0])-1 :
        temp += translate(grid[x-1][y+1])
    else:
        temp+= translate(val)
        #print ( "top right" + temp)

    if y > 0 :
        temp += translate(grid[x][y-1])
    else:
        temp+= translate(val)
    temp += translate(grid[x][y])
    if y < len(grid[0])-1 :
        temp += translate(grid[x][y+1])
    else:
        temp+= translate(val)
    if y > 0 and x < len(grid) -1 :
        temp += translate(grid[x+1][y-1])
    else:
        temp+= translate(val)
    if x < len(grid)-1  :
        temp += translate(grid[x+1][y])
    else:
        temp+= translate(val)
    if x < len(grid)-1 and y < len(grid[0])-1:
        temp += translate(grid[x+1][y+1])
    else:
        temp+= translate(val)
    return temp

if __name__ == '__main__':
    args = parse_args()
    input = open(args.path, 'r').read()[:-1].split('\n')
    enhancement = input[0]
    grid = []
    for i in input[2:]:
        grid.append(i)

    bigger_grid = ["." * (len(grid[0])+200)]*100
    for i in range(0,len(grid)):
        temp_line = "."*100
        for j in range ( 0, len(grid[0])):
            temp_line += ( grid[i][j])
        temp_line += "."*100
        bigger_grid.append(temp_line)
    temp_tab = ["." * (len(grid[0])+200)]*100
    bigger_grid += (temp_tab)
    for i in bigger_grid:print(i)

    print ("FIRST ITERATION")
    for i in range(0,50):
        print(i)
        new_grid = []
        print(bigger_grid[0][0])
        char = bigger_grid[0][0]
        val = "."
        print ("first" + char)
        if char == ".":
            val == "#"
            print ("val" + val)
        for i in range(0,len(bigger_grid)):
            #temp_line = "#"
            temp_line = ""
            for j in range ( 0, len(bigger_grid[0])):
                #print (get_number(bigger_grid,i,j))
                temp_line += ( enhancement[int(get_number(bigger_grid, i, j, char),2)])
            #temp_line += "#"
            new_grid.append(temp_line)
        #new_grid.append("#" * (len(bigger_grid[0])+2))
        #for i in new_grid:print(i)
        bigger_grid = new_grid

        for i in bigger_grid:print(i)
    count = 0
    for i in new_grid[2:-2]:
        count += i[2:-2].count("#")
    print (count)
