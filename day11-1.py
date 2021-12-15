#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

DIM = 10
COUNT = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def propagate(table):
    global COUNT
    for k in range(0,100):
        for i in range(0, DIM):
            for j in range(0,DIM):
                if table[i][j]>9:
                    if i+1 < DIM and table[i+1][j] != -1: table[i+1][j]+=1
                    if j+1 < DIM and table[i][j+1] != -1: table[i][j+1] +=1
                    if i-1 >=0 and table[i-1][j] != -1: table[i-1][j] +=1
                    if j-1 >= 0 and table[i][j-1] != -1: table[i][j-1] +=1
                    if i-1 >=0  and j-1 >= 0 and table[i-1][j-1] != -1: table[i-1][j-1] +=1
                    if i+1 < DIM and j-1 >= 0 and table[i+1][j-1] != -1: table[i+1][j-1] +=1
                    if i+1 < DIM  and j+1 < DIM and table[i+1][j+1] != -1: table[i+1][j+1] +=1
                    if i-1 >= 0 and j+1 < DIM and table[i-1][j+1] != -1: table[i-1][j+1] +=1
                    table[i][j] = -1

    for i in range(0, DIM):
        for j in range(0,DIM):
            if table[i][j] == -1 :
                table[i][j]=0
                COUNT +=1
    print ("============")
    for i in table:
        print(''.join(str(e) for e in i))
    return table


def first_blink (table):
    output = []
    for line in table:
        out_line = []
        for x in line:
            out_line.append (int(x) + 1)
        output.append(out_line)
    return output

def process (inputs):
    output = inputs
    for k in range(0,100):
        output = first_blink (output)
        output = propagate(output)
    return output

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    for line in inputs:
        for x in line :
            x = int(x) + 1
    print (process(inputs))
    print(COUNT)
