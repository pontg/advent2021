#!/usr/bin/env python

import argparse
import sys
from collections import defaultdict
import ast

class tree():
    def __init__(self, input, depth = 0, parent = None):
        self.input = input
        self.depth = depth
        self.parent = parent
        self.value = -1
        #print(self.depth, input,  isinstance(input, list))
        if isinstance(input, int):
            self.value = input
            self.leaf = True
        else:
            self.leaf = False
            self.left = tree(input[0], depth + 1, self)
            self.right = tree(input[1], depth + 1, self)

    def split(self):
        print ("split")
        lnode = tree(int(self.value // 2), self.depth + 1, self)
        rnode = tree(int(self.value - self.value // 2), self.depth + 1, self)
        self.left = lnode
        self.right = rnode
        self.leaf = False

    def explode(self):
        print (f"explooooooooooooose" + printtree(self))
        next_left = self
        broke_left = False
        while next_left.depth !=1 and next_left == next_left.parent.left:
            next_left = next_left.parent
        if next_left == next_left.parent.left:
            print ("no left neighbor ->0")
        else:
            rightest = next_left.parent.left
            while not rightest.leaf:
                rightest = rightest.right
            print("yoloooooooooooooooooooooooooooooooo " + str(rightest.value))
            rightest.value += self.left.value
            print(" updated yoloooooooooooooooooooooooooooooooo " + str(rightest.value))
        next_right = self
        broke_right = False
        while next_right.depth !=1 and next_right == next_right.parent.right:
            next_right = next_right.parent
        if next_right == next_right.parent.right:
            print ("no right neighbor ->0")
        else:
            leftest = next_right.parent.right
            while not leftest.leaf:
                leftest = leftest.left
            leftest.value += self.right.value
        self.value = 0
        self.leaf = True
        self.right = None
        self.left = None
        return

    def traverse_split(self):
        if self.leaf:
            if self.value>9:
                return self
            return None
        else:
            spn =self.left.traverse_split()
            if spn == None:
                return self.right.traverse_split()
            return spn


    def traverse(self, explosion = False, check_split = False):
        #print(self.depth, check_split)
        left = self.left
        right = self.right
        split = None
        if self.depth == 4:
            print(printtree(self))
            self.explode()
            print(printtree(self))

            explosion = True
        else:
            if not left.leaf:
                #print ("traverse left")
                explosion = left.traverse(explosion, check_split)
            if not right.leaf:
                #print ("traverse right")
                explosion =right.traverse(explosion, check_split)
        #print(printtree(self))
        return explosion


    def __str__ (self):
        if self.leaf:
            return (f"depth: {self.depth}, value: {self.value}\n" )
        else:
            return (f"depth: {self.depth}, left: {self.left}, right: {self.right}")

def printtree(tree):
    str = ""
    if tree.leaf:
        str = tree.value
    else:
        str = "[{},{}]".format(printtree(tree.left), printtree(tree.right))
    return str

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True)

    return parser.parse_args()

def magnitude (tree):
    if tree.left.leaf and tree.right.leaf:
        return 3 * tree.left.value + 2 * tree.right.value
    elif tree.left.leaf:
        return 3 * tree.left.value + 2 * magnitude(tree.right)
    elif tree.right.leaf:
        return 3* magnitude(tree.left) + 2 * tree.right.value
    else:
        return 3* magnitude(tree.left) + 2 * magnitude(tree.right)

if __name__ == '__main__':
    args = parse_args()
    input = open(args.path, 'r').read()[:-1].split('\n')
    input_list = []
    for i in input:
        input_list.append(ast.literal_eval(i))
    print (input_list)
    add = input_list[0]
    for i in input_list[1:]:
        add = [add,i]
        print (add)
        t = tree(add)
        continu = t.traverse()
        print(printtree(t))

        while (continu):
            explosion = t.traverse(False, continu)
            print(printtree(t))
            if (not explosion ):
                split = t.traverse_split()
                if split != None:split.split()
            continu = explosion or split != None
        add = ast.literal_eval(printtree(t))

    print ("============")
    print(printtree(t))
    print(magnitude(t))
