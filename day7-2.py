#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests


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
            steps = abs(int(inputs[int(l)]) - k)
            burnt_this_round = 0
            for i in range (0,steps):
                burnt_this_round +=  (steps-i)
            fuel[k][l] = burnt_this_round
    burnt = [ sum(i) for i in fuel]
    print(min(burnt))
    print(burnt.index(min(burnt)))
