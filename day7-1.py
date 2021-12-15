#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests
from statistics import median


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split(',')
    fuel = []
    max = max([int(n) for n in inputs])
    for i in range(0,max):
        temp = []
        for j in range(0, len(inputs)) :
            temp.append([0])
        fuel.append(temp)

    for k in range(0,max):
        for l in range(0, len(inputs)) :
            fuel[k][l] = (abs(int(inputs[int(l)]) - k))
    burnt = [ sum(i) for i in fuel]
    #print(burnt)
    print(min(burnt))
    print(burnt.index(min(burnt)))
    sorted = inputs.sort()
    print(inputs)
    test = []
    for i in inputs :
        test.append(int(i))
    test.sort()
    print(median(test))
