#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

COUNT = 0
LIST = []

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def dive( paths, blocked, start, output, visited_once,joker ):
    global COUNT
    global LIST
    new_out = []
    matches = []
    for line in paths:
        if start in line:
            matches.append(line)
    if joker and start.islower():
        blocked.append(start)
    if start.islower() and start not in visited_once:
        visited_once.append(start)
    elif start.islower():
        blocked.append(start)
        for i in visited_once:
            blocked.append(i)
        joker = True
    while matches :
        new_out_l = output.copy()
        next = matches[0].copy()
        new_visited_once = visited_once.copy()
        next.remove(start)
        counterpart = next[0]
        new_blocked = blocked.copy()
        #if counterpart.islower() and counterpart != 'end' :
        #    if counterpart not in new_visited_once:
        #        new_visited_once.append(counterpart)
        #    else:
        #        if joker:
        #            new_blocked.append(counterpart)
        #        else:
        #            joker = True


        #if joker and start in new_visited_once:
        #    new_blocked.append(start)
        if counterpart not in new_blocked   :
            new_out_l.append(start)
            if counterpart != 'end' :
                dive(paths, new_blocked, counterpart, new_out_l, new_visited_once, joker)
            else:
                print(" FOUND THE END")
                new_out_l.append('end')
                print (new_out_l)
                COUNT +=1
                LIST.append(new_out_l)
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
        visited_once = []
        blocked = []
        blocked.append('start')
        start = starts[0].copy()
        start.remove('start')
        counterpart = start[0]
        print (counterpart)
        output.append('start')
        #if counterpart.islower():
        #    visited_once.append(counterpart)
        if counterpart != 'end':
            dive(paths, blocked, counterpart, output, visited_once, False)
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
    temp = []
    for j in LIST:
        temp.append(''.join(str(e) for e in j))
        #print(temp)
    print (len(list(dict.fromkeys(temp))))
