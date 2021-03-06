#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def get_neighbors(i, j, max_i, max_j):
    temp = []
    if i+1 < max_i :
        temp.append((i+1,j))
    if j+1 < max_j :
        temp.append((i,j+1))
    if i > 0 :
        temp.append((i-1,j))
    if j > 0  :
        temp.append((i,j-1))
    return temp

if __name__ == '__main__':
    args = parse_args()
    inputs = open(args.path, 'r').read()[:-1].split('\n')
    table = []
    risks = []
    for i in inputs:
        temp = []
        temp_void = []
        for j in i:
            temp.append(j)
            temp_void.append(0)
        table.append(temp)
        risks.append(temp_void)
    visited = [(0,0)]
    unvisited =[]
    height = len(table)
    width = len(table[0])

    for n in range(height):
        for m in range(width):
            unvisited.append((n,m))
    shortest_path = defaultdict(lambda:2000)
    shortest_path[(0,0)] = 0
    previous_nodes = defaultdict(list)

    while unvisited:
        current_min_node = None
        for node in unvisited:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = get_neighbors(current_min_node[0], current_min_node[1], height, width)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + int(table[neighbor[0]][neighbor[1]])
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
        unvisited.remove(current_min_node)
    print (previous_nodes, shortest_path)
