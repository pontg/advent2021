#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def count_deeper_ticks(list: List[int]) -> int:
    count = 0
    for i in range(1, len(list)):
        if int(list[i]) > int(list[i-1]):
            count += 1
    return count

if __name__ == '__main__':
    args = parse_args()
    depth_ticks = open(args.path, 'r').read()
    print(count_deeper_ticks(depth_ticks.split()))
