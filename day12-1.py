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

def dive( paths, blocked, start, output ):
    global COUNT
    new_out = []
    matches = []
    #print(start)
    #print(output)
    for line in paths:
        if start in line:
            matches.append(line)
    iter = []
    print("matches")
    print(matches)
    while matches :
        new_out_l = output.copy()
        next = matches[0].copy()
        next.remove(start)
        counterpart = next[0]
        new_blocked = blocked.copy()
        print("blocked")

        print(blocked)
        if counterpart not in new_blocked:
            new_out_l.append(start)

            if counterpart.islower() and counterpart != 'end' :
                new_blocked.append(counterpart)
                #print(blocked)
            if counterpart != 'end':
                #print ( "diving:" + counterpart)
                dive(paths, new_blocked, counterpart, new_out_l)
            else:
                print(" FOUND THE END")
                new_out_l.append('end')
                print (new_out_l)
                COUNT +=1
            new_out.append(new_out_l)
        matches.pop(0)
    return new_out

def traverse( paths, blocked):
    starts = []
    for line in paths:
        if 'start' in line:
            starts.append(line)
    print(starts)
    iter = []
    outputs =[]
    while(starts):
        output = []
        blocked = []
        blocked.append('start')
        start = starts[0].copy()
        start.remove('start')
        counterpart = start[0]
        print (counterpart)
        output.append('start')
        if counterpart.islower():
            blocked.append(counterpart)
        if counterpart != 'end':
            dive(paths, blocked, counterpart, output)
        starts.pop(0)
        outputs.append(output)
    print ("============")
    for i in outputs:
        print(output)


if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    paths = []
    blocked = []
    for i in inputs:
        paths.append(i.split('-'))
    traverse(paths, blocked)
    print (COUNT)
