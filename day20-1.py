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

def get_number(grid,x,y):
    temp = ""
    if y > 0 and x > 0:
        temp += translate(grid[x-1][y-1])
    else:
        temp+= "0"
    if x > 0 :
        temp += translate(grid[x-1][y])
    else:
        temp+= "0"
    if x >0 and y < len(grid[0])-2 :
        temp += translate(grid[x-1][y+1])
    else:
        temp+= "0"
    if y > 0 :
        temp += translate(grid[x][y-1])
    else:
        temp+= "0"
    temp += translate(grid[x][y])
    if y < len(grid[0])-2 :
        temp += translate(grid[x][y+1])
    else:
        temp+= "0"
    if y > 0 and x < len(grid) -2 :
        temp += translate(grid[x+1][y-1])
    else:
        temp+= "0"
    if x < len(grid)-2  :
        temp += translate(grid[x+1][y])
    else:
        temp+= "0"
    if x < len(grid)-2 and y < len(grid[0])-2:
        temp += translate(grid[x+1][y+1])
    else:
        temp+= "0"
    return temp

if __name__ == '__main__':
    args = parse_args()
    input = open(args.path, 'r').read()[:-1].split('\n')
    enhancement = input[0]
    grid = []
    for i in input[2:]:
        grid.append(i)

    bigger_grid = ["." * (len(grid[0])+200)]*10
    for i in range(0,len(grid)):
        temp_line = "."*100
        for j in range ( 0, len(grid[0])):
            temp_line += ( grid[i][j])
        temp_line += "."*100
        bigger_grid.append(temp_line)
    temp_tab = ["." * (len(grid[0])+200)]*10
    bigger_grid += (temp_tab)
    for i in bigger_grid:print(i)

    print ("FIRST ITERATION")
    new_grid = []
    for i in range(0,len(bigger_grid)):
        #temp_line = "#"
        temp_line = ""
        for j in range ( 0, len(bigger_grid[0])):
            #print (get_number(bigger_grid,i,j))
            if i == 0 and j ==1:
                print (get_number(bigger_grid,i,j))
            temp_line += ( enhancement[int(get_number(bigger_grid, i, j),2)])
        #temp_line += "#"
        new_grid.append(temp_line)
    #new_grid.append("#" * (len(bigger_grid[0])+2))
    for i in new_grid:print(i)

    print ("SECOND ITERATION")
    new_grid1 = []
    for i in range(0,len(new_grid)):
        #temp_line = "."
        temp_line = ""
        for j in range ( 0, len(new_grid[0])):
            #print (get_number(bigger_grid,i,j))
            if i == 0 and j ==1:
                print (get_number(new_grid,i,j))
            temp_line += ( enhancement[int(get_number(new_grid, i, j),2)])
        #temp_line += "."
        new_grid1.append(temp_line)
    #new_grid1.append("." * (len(new_grid[0])+2))
    for i in new_grid1:print(i)

    count = 0
    for i in new_grid1[:-2]:
        count += i[:-2].count("#")
    print (count)
