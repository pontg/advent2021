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
    pairs = {}
    rule_patterns = []
    rule_letter = []
    for i in range(2,len(inputs)):
        temp = inputs[i].split(' -> ')
        rule_patterns.append(temp[0])
        rule_letter.append(temp[1])
        inserts.append( temp[0][0] + temp[1] + temp [0][1])
        #pairs.append(temp[0][0]+temp[0][1], 0)
    outputs = []
    for char_i in range(0,len(polymer)-1):
        pairs[polymer[char_i]+polymer[char_i+1]] =1
    print(pairs)
    for k in range(0,10):
        print("=========")
        cop = pairs.copy()
        for p in cop:
            if p in rule_patterns and cop[p]>0:
                #pairs[p] = cop[p]
                pairs[p] -= cop[p]
                index = rule_patterns.index(p)
                first_letter = rule_patterns[index][0]
                new_letter = rule_letter[index]
                last_letter = rule_patterns[index][1]
                prev_pattern = rule_patterns[index][0]+rule_letter[index]
                print (prev_pattern)
                if prev_pattern not in cop:
                    pairs[prev_pattern] = cop[p]
                else:
                    print ("increase")
                    pairs[prev_pattern] += cop[p]
                if rule_letter[index] + rule_patterns[index][1] not in pairs.values():
                    pairs[rule_letter[index] + rule_patterns[index][1]] = cop[p]
                else:
                    pairs[rule_letter[index] + rule_patterns[index][1]] += cop[p]
        for p in pairs:
            print( p, pairs[p])

    count_letters = {}
    for p in pairs:
        if p[0] not in count_letters:
            count_letters[p[0]] = pairs[p]
        else:
            count_letters[p[0]] += pairs[p]
    print (count_letters)
