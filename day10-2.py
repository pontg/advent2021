#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests
from statistics import median


CHARS = ['(',')','[',']','{','}','<','>']
VALUES= [1,1,2,2,3,3,4,4]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def complete2(line):
    output = []
    for i in range(0,len(line)):
        if line[i] in ['(', '[','{','<']:
            substr = line[i:]
            #print(substr)
            opener = line[i]
            opener_index = CHARS.index(line[i])
            closer = CHARS[opener_index + 1]
            if closer in substr:
                closer_index = substr.index(closer)
            else :
                closer_index = len(line)
            substring = substr[:closer_index+1]
            openers = substr.count(opener)
            closers = substr.count(closer)
            #print(substring)
            #substring.index(closer)
            if  openers > closers :
                if substring.count(opener) != substring.count(closer):
                    #print(closer)
                    output.append(closer)
    return list(reversed(output))


def complete(line):
    output = []
    for i in range(0,len(line)):
        if line[i] in ['(', '[','{','<']:
            substr = line[i:]
            #print(substr)
            opener = line[i]
            opener_index = CHARS.index(line[i])
            closer = CHARS[opener_index + 1]
            if closer in substr:
                closer_index = substr.index(closer)
            else :
                closer_index = len(line)
            substring = substr[:closer_index+1]
            openers = substr.count(opener)
            closers = substr.count(closer)
            #print(substring)
            #substring.index(closer)
            max = len(line)
            ok = False
            while max > i:
                if closer in line[i:max]:
                    openersl = line[i:max].count(opener)
                    closersl = line[i:max].count(closer)
                    if  openersl == closersl :
                        ok = True
                        break
                max = max -1
            if  openers > closers and ok == False:
                if substring.count(opener) != substring.count(closer):
                    #print(closer)
                    output.append(closer)
    return list(reversed(output))

def is_valid (substr):
    counts = [0,0,0,0,0,0,0,0]
    valid = False
    opening = CHARS[CHARS.index(substr[-1])-1]

    subsubstring = ''
    count_o = 0
    count_c = 1
    max = len(substr)
    for i,v in reversed(list(enumerate(substr[:-1]))):
        if v == opening:
            count_o+=1
        if v == substr[-1]:
            count_c+=1
        if count_o == count_c:
            subsubstring = substr[i:]
            step = max
        if subsubstring != '':break

    if subsubstring == '':
        #print("ALARM" + substr[-1])
        return VALUES[CHARS.index(substr[-1])]
    for k in subsubstring:
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
    if ( counts[0] + counts[2] + counts[4] + counts[6] == counts[1] + counts[3] + counts[5] + counts[7]):
        valid = True
    else :
        #print ("ALARM " + substr[-1])
        return VALUES[CHARS.index(substr[-1])]
    return 0

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    incomplete = []
    for i in inputs:
        error = 0
        for j in range(0, len(i)):
            if i[j] in [')', ']','}','>']:
                #print (i)
                if is_valid(i[0:j+1]) != 0:
                    error += is_valid(i[0:j+1])
                    break
        if error == 0:
            incomplete.append(i)
    result = []
    print(len(incomplete))
    for line in incomplete:
        result.append(complete(line))
    total = 0
    tot = []
    print(result)
    for i in result:
        total = 0
        for j in i:
            total = 5* total + VALUES[CHARS.index(j)]
        tot.append(total)
    print(median(tot))
