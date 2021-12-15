#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

CHARS = ['(',')','[',']','{','}','<','>']
VALUES= [3,3,57,57,1197,1197,25137,25137]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def poubelle():
    if counts[0] < counts[1]:
        print (3)
    if counts[2] < counts[3]:
        print (57)
    if counts[4] < counts[5]:
        print (1197)
    if counts[6] < counts[7]:
        print (25137)

    print(counts)
    if j == '(':
        counts[0]+=1
    if j == ')':
        counts[1]+=1
    if j == '[':
        counts[2]+=1
    if j == ']':
        counts[3]+=1
    if j == '{':
        counts[4]+=1
    if j == '}':
        counts[5]+=1
    if j == '<':
        counts[6]+=1
    if j == '>':
        counts[7]+=1

def is_valid (substr):
    counts = [0,0,0,0,0,0,0,0]
    valid = False
    #print ("is valid ?")
    #print(substr)
    opening = CHARS[CHARS.index(substr[-1])-1]
    #print(opening)
    # find closest opening
    subsubstring = ''
    count_o = 0
    count_c = 1
    max = len(substr)
    for i,v in reversed(list(enumerate(substr[:-1]))):
        #print(i,v)
        if v == opening:
            count_o+=1
        if v == substr[-1]:
            count_c+=1
        #print (count_o,count_c)

        if count_o == count_c:
            #print("found")
            subsubstring = substr[i:]
            step = max
        if subsubstring != '':break

    if subsubstring == '':
        #print("ALARM" + substr[-1])
        return VALUES[CHARS.index(substr[-1])]
    #print(subsubstring)
    for k in subsubstring:
        #print(i[k])
        #print(k)
        if k == '(':
            counts[0]+=1
        if k == ')':
            counts[1]+=1
        if k == '[':
            counts[2]+=1
        if k == ']':
            counts[3]+=1
        if k == '{':
            counts[4]+=1
        if k == '}':
            counts[5]+=1
        if k == '<':
            counts[6]+=1
        if k == '>':
            counts[7]+=1
        #print (counts)
    if ( counts[0] + counts[2] + counts[4] + counts[6] == counts[1] + counts[3] + counts[5] + counts[7]):
        valid = True
        #print("ok")
    else :
        #print ("ALARM " + substr[-1])
        return VALUES[CHARS.index(substr[-1])]
    return 0

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    #        [(,),[,],{,},<,>]
    error = 0
    for i in inputs:
        #print(i)
        for j in range(0, len(i)):
            #counts = [0,0,0,0,0,0,0,0]

            if i[j] in [')', ']','}','>']:
                #print (i)
                if is_valid(i[0:j+1]) != 0:
                    error += is_valid(i[0:j+1])
                    break
    print(error)
            #print (counts)
            #if ( counts[0] + counts[2] + counts[4] + counts[6] < counts[1] + counts[3] + counts[5] + counts[7]):
            #    print(j)
            #    break
            #if counts[0] < counts[1]:
            #    print (3)
            #    break
            #if counts[2] < counts[3]:
            #    print (57)
            #    break
            #if counts[4] < counts[5]:
            #    print (1197)
            #    break
            #if counts[6] < counts[7]:
            #    print (25137)
            #    break

        #print (counts)
