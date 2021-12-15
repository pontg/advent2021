#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests
from collections import defaultdict

COUNT = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    polymer = inputs[0]
    inserts = []
    pairs = defaultdict(int)
    rule_patterns = []
    rule_letter = []
    for i in range(2,len(inputs)):
        temp = inputs[i].split(' -> ')
        rule_patterns.append(temp[0])
        rule_letter.append(temp[1])
        inserts.append( temp[0][0] + temp[1] + temp [0][1])
    outputs = []
    for char_i in range(0,len(polymer)-1):
        pairs[polymer[char_i]+polymer[char_i+1]] = 1
    for k in range(0,40):
        for p,v in (pairs.copy().items()):
            print(p,v)
            index = rule_patterns.index(p)
            first_letter = rule_patterns[index][0]
            new_letter = rule_letter[index]
            last_letter = rule_patterns[index][1]
            prev_pattern = rule_patterns[index][0]+rule_letter[index]
            next_pattern = new_letter + last_letter
            pairs[next_pattern] += v
            pairs[prev_pattern] += v
            pairs[p] -= v

    count_letters = defaultdict(int)
    for p in pairs:
        count_letters[p[0]] += pairs[p]
    count_letters[polymer[-1]] += 1
    print (count_letters)
