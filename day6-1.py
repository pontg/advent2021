#!/usr/bin/env python

import argparse
import sys
from typing import List
import requests

class lanternfish:
    def __init__(self, is_newborn, timer):
        self.is_newborn = is_newborn
        self.spawn_timer = 0
        if is_newborn:
            self.spawn_timer = 8
        else:
            if timer == None:
                self.spawn_timer = 6
            else :
                self.spawn_timer = timer

    def pretty_print(self):
        print ("is newborn " + str(self.is_newborn))
        print (" next spawn in " + str(self.spawn_timer) + " days")

    def decrease_spawn_timer(self):
        self.spawn_timer -= 1
        self.is_newborn = False

    def reset_clock(self):
        self.spawn_timer = 6


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def count_fish(fish_school, days_limit):
    i = 0
    for i in range(0, days_limit):
        append_count = 0

        for lantern in fish_school:
            #print (lantern.spawn_timer)
            if lantern.spawn_timer == 0:
                append_count += 1
                lantern.reset_clock()
            else :
                lantern.decrease_spawn_timer()
                #lantern.pretty_print()
        for i in range(0,append_count):
            fish_school.append(lanternfish(True, None))
    return fish_school

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1]
    school = []
    days_limit = 256
    for i in inputs.split(','):
        fish = lanternfish(False, int(i))
        #print(fish.pretty_print())
        school.append(fish)
    print (len(count_fish(school, days_limit)))
