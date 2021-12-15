#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    values = []
    un,quatre,sept,huit = 0,0,0,0
    for line in inputs:
        print(line)
        for i in range(11,15):
                j = line.split(' ')
                if len(j[i]) == 2:
                    un +=1
                if len(j[i]) == 4:
                    quatre +=1
                if len(j[i]) == 3:
                    sept +=1
                if len(j[i]) == 7:
                    huit +=1
    print (un + quatre + sept + huit)
