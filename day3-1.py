#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def brute_force( lines: List[ord]) -> int:
    length = len(lines[0])
    count_zeros = [0]*length
    # it was actually not necessary to count 0s ...
    count_ones = [0]*length
    gamma = ""
    epsilon = ""
    for line in lines:
        for i in range(0,len(line)):
            if line[i] == '0' :
                count_zeros[i] += 1
            else:
                count_ones[i] += 1
    for i in range(0,len(lines[1])):
        if count_ones[i] > count_zeros[i]:
            gamma+='1'
            epsilon+='0'
        else:
            gamma+='0'
            epsilon+='1'
    return int(gamma,2)*int(epsilon,2)

if __name__ == '__main__':
    args = parse_args()
    report = open(args.path, 'r').read()
    print(brute_force(report.split()))
