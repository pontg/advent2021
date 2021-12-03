#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def aggregate_depths(list: List[int]) -> List[int]:
    aggregate_depths = []
    for i in range(2, len(list)):
        aggregate_depths.append(int(list[i-1])+int(list[i-2])+int(list[i]))
    return aggregate_depths


def count_deeper_ticks(piou: List[int]) -> int:
    count = 0
    for i in range(1, len(piou)):
        if int(piou[i]) > int(piou[i-1]):
            count += 1
    return count

if __name__ == '__main__':
    args = parse_args()
    depth_ticks = open(args.path, 'r').read()
    print(count_deeper_ticks(aggregate_depths(depth_ticks.split())))
