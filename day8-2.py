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
    omega_somme = 0
    for line in inputs:
        zero,un,deux,trois,quatre,cinq,six,sept,huit,neuf = '','','','','','','','','',''
        found = 0
        j = line.split(' ')
        while found < 11:
            for i in range(0,10):
                if len(j[i]) == 2 and un =='' :
                    un = j[i]
                elif len(j[i] ) == 4 and quatre =='':
                    quatre = j [i]
                elif len(j[i]) == 3  and sept =='':
                    sept = j[i]
                elif len(j[i])  == 7 and huit =='':
                    huit = j[i]
                elif len(j[i]) == 5 and trois =='' and un != '':
                    if ( un[0] in j[i] and un[1] in j[i]):
                        trois = j[i]
                elif len(j[i]) == 6 and neuf =='' and trois != '':
                    if ( trois[0] in j[i] and trois[1] in j[i] and trois[2] in j[i] and trois[3] in j[i] and trois[4] in j[i]):
                        neuf = j[i]
                elif len(j[i]) == 6 and zero == '' and sept != '' and neuf != '':
                    if sept[0] in j[i] and sept[1] in j[i] and sept[2] in j[i]:
                        zero = j[i]
                elif len(j[i]) == 6 and zero != '' and neuf != '' and neuf != j[i] and six == '':
                    six = j[i]
                elif len(j[i]) == 5 and quatre != '' and un != '' and trois != '':
                    temp_mask = ''
                    for n in quatre:
                        if n not in un:
                            temp_mask += n
                    if temp_mask[0] in j[i] and temp_mask[1] in j[i]:
                        cinq = j[i]
                    if (temp_mask[0] not in j[i]) or (temp_mask[1] not in j[i]):
                        if deux == '' and j[i] != trois :
                            deux = j[i]
            found +=1
        digits = ''
        print( "--------")
        for k in range (11,15):
            if sorted(j[k]) == sorted(zero):
                digits+='0'
            if sorted(j[k]) == sorted(un):
                digits+='1'
            if sorted(j[k]) == sorted(deux):
                digits+='2'
            if sorted(j[k]) == sorted(trois):
                digits+='3'
            if sorted(j[k]) == sorted(quatre):
                digits+='4'
            if sorted(j[k]) == sorted(cinq):
                digits+='5'
            if sorted(j[k]) == sorted(six):
                digits+='6'
            if sorted(j[k]) == sorted(sept):
                digits+='7'
            if sorted(j[k]) == sorted(huit):
                digits+='8'
            if sorted(j[k]) == sorted(neuf):
                digits+='9'
        print(digits)
        omega_somme += int(digits)
    print(omega_somme)
