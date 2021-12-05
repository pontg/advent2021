#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def most_common_first_bit(lines:List[ord], position:int) -> str:
    count_one = 0
    for line in lines:
        if line[position] == '1' : count_one += 1

    output = '0'
    if count_one >= len(lines)/2 : output = '1'
    return output

def least_common_first_bit(lines:List[ord], position:int) -> str:
    count_zeros = 0
    for line in lines:
        if line[position] == '0' : count_zeros += 1

    output = '0'
    if count_zeros > len(lines)/2 : output = '1'
    return output

def oxygen (lines:List[ord], position:int) -> str:
    bit = most_common_first_bit(lines, position)
    #print(bit)
    next = []
    for line in lines:
        if line[position] == bit:
            next.append(line)
    if len(next) == 1 :
        #print("oxygen: " + next[0])
        return next[0]
    else :
        return oxygen(next, position+1)

def scraper(lines:List[ord], position:int) -> str:
    bit = least_common_first_bit(lines, position)
    #print(bit)
    next = []
    for line in lines:
        if line[position] == bit:
            next.append(line)
    if len(next) == 1 :
        #print("scrape: " + next[0])
        return next[0]
    else :
        return scraper(next, position+1)

if __name__ == '__main__':
    args = parse_args()
    report = open(args.path, 'r').read()
    print(oxygen(report.split(), 0))
    print(scraper(report.split(), 0))
