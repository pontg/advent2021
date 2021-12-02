#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser(description='yolo', usage=' I said yolo !')
    #parser.add_argument('--url', required=True) ## actually stupid, need to be logged in to get your private list
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def track_position( instructions: List[str]) -> int:
    depth = 0
    horizontal = 0
    aim = 0
    for instruction in instructions:
        if instruction.split()[0] == "forward" :
            horizontal += int(instruction.split()[1])
            depth += aim * int(instruction.split()[1])
        if instruction.split()[0] == "up" :
            aim -= int(instruction.split()[1])
        if instruction.split()[0] == "down" :
            aim += int(instruction.split()[1])
    return depth * horizontal

if __name__ == '__main__':
    args = parse_args()
    instructions = open(args.path, 'r').read()
    #splicing last element to avoid the last empty item created by the last linebreak
    print(track_position(instructions.split('\n')[:-1]))
