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

def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq


if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    polymer = inputs[0]
    inserts = []
    for i in range(2,len(inputs)):
        temp = inputs[i].split(' -> ')
        inserts.append( temp[0][0] + temp[1] + temp [0][1])
    #print (inserts)
    #print (polymer)
    outputs = []
    for k in range(0,40):
        new_polymer = []
        for char_i in range(0,len(polymer)-1):
            found = False
            for insert in inserts:
                if polymer[char_i] == insert[0] and polymer[char_i+1] == insert[2]:
                    new_polymer.append(insert[0:2])
                    found = True
            if not found:
                new_polymer.append(polymer[char_i])
        new_polymer.append(polymer[-1])
        outputs.append(new_polymer)
        #print(new_polymer)
        polymer = ''.join(new_polymer)



    #for output in outputs:
    #    print(''.join(output))
    final_polymer = ''.join(outputs[-1])
    print (check_freq(final_polymer))
