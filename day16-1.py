#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict
from math import prod

COUNT = 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

class packet ():
    def __init__(self, input):
        global COUNT
        #print ("new packet" + input)
        self.block = input
        self.version = input[0:3]
        COUNT += int(self.version,2)
        self.type = int(input[3:6],2)
        self.child = []
        self.value = -1
        if self.type == 4:
            print("litteral")
            temp = ''
            sub_block = input[6:]
            #print(sub_block)
            count = 0
            while sub_block[0] != '0':
                #print(sub_block)
                temp += sub_block[1:5]
                sub_block = sub_block[5:]
                count += 1
            temp += sub_block[1:5]
            self.rest = sub_block[5:]
            self.length = count + 1
            self.value = int(temp,2)
            #print("rest" + self.rest)
            #print(temp, self.value)
        else:
            self.length_type = input[6]
            if self.length_type == '0':
                #print ( "parse by length")
                temp_block = input[7:22]
                #print(temp_block)
                self.length = int(temp_block,2)
                current_block = input[22:22+self.length]
                next_block = input[22+self.length:]

                self.child.append(packet(input[22:22+self.length]))
                iter = 22
                while len(self.child[-1].rest) != 0:
                    iter += self.length
                    self.child.append(packet(self.child[-1].rest))
                self.rest = input[22+self.length:]
                #self.child.append(packet(input[22+self.length:]))
            else :
                #print ( "parse by count")
                temp_block = input[7:18]
                self.nb = int(temp_block,2)
                self.child.append(packet(input[18:]))
                for i in range(self.nb - 1):
                    self.child.append(packet(self.child[-1].rest))
                self.rest = self.child[-1].rest

    def evaluate(self):
        #for i in self.child:
            #print(i.__str__())
        if self.value != -1:
            print ("leaf: " + str(self.value))
            return self.value
        if self.type == 0:
            self.value = sum(children.evaluate() for children in self.child)
        if self.type == 1:
            self.value = prod(children.evaluate() for children in self.child)
        if self.type == 2:
            self.value = min(children.evaluate() for children in self.child)
        if self.type == 3:
            self.value = max(children.evaluate() for children in self.child)
        if self.type == 5:
            self.value = 0
            if self.child[0].evaluate()> self.child[1].evaluate():
                self.value = 1
        if self.type == 6:
            self.value = 0
            if self.child[0].evaluate() < self.child[1].evaluate():
                self.value = 1
        if self.type == 7:
            self.value = 0
            if self.child[0].evaluate() == self.child[1].evaluate():
                self.value = 1
        print( "value" + str(self.value))
        return self.value


    def __str__ (self):


        out = "value: " + str(self.value) + " type: "
        if self.type == 0:
            out += 'sum: '
        if self.type == 1:
            out += 'prod: '
        if self.type == 2:
            out += 'max: '
        if self.type == 3:
            out += 'min: '
        if self.type == 5:
            out += '>: '
        if self.type == 6:
            out += '<: '
        if self.type == 7:
            out += '==: '
        for i in self.child:
            out += str(i.value) +","
        return out

def parse_block( block):
    pack = packet(block)
    print(pack.__str__())
    print (pack.evaluate())
    print (pack.value)


if __name__ == '__main__':
    args = parse_args()
    input = open(args.path, 'r').read()[:-1]#.split('\n')
    print(input)
    end_length = len(input) * 4
    hex_as_int = int(str(input), 16)
    binary =bin(hex_as_int)
    padded_binary = binary[2:].zfill(end_length)
    print(padded_binary)
    parse_block(padded_binary)

    #print ( "COUNT" + str(COUNT))
