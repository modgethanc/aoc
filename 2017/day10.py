#!/usr/bin/python3

"""
AOC 2017 Day :
"""

import sys
import itertools
from shortcuts import *

def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()


    print("part one solution: " + str(solve_part_one(256, inputs[0])))
    print("part two solution: " + str(solve_part_two(256, inputs[0])))

    return 0

def solve_part_one(size, inputs):
    """
    Solver for part one.
    """

    lengths = intify(inputs.split(","))

    skip = 0
    position = 0
    knot = make_string(size)

    #print("starting: "+str(knot))

    for length in lengths:
        start = position
        end = (start + length - 1) % size

        # swap magic
        left = newleft = start
        right = newright = end
        #print("original start "+str(start))
        #print("original end "+str(end))

        swaps = length // 2
        i = 0

        while i < swaps:
            left = newleft
            right = newright
            #print("left:" + str(left))
            #print("right:" + str(right))
            (knot[left], knot[right]) = (knot[right], knot[left])
            newleft = (left + 1) % size
            newright = (right - 1) % size
            #print(knot)
            #print("new left: "+ str(newleft) + " new right: "+str(newright))

            i += 1


        position += skip + length
        position %= size
        skip += 1

    #print("ending: "+str(knot))

    return knot[0]*knot[1]

def make_string(length):
    """
    Generates a list of ints of the given length. This feels clunky, but here
    we are.
    """

    i = 0
    blank_string = []

    while i < length:
        blank_string.append(i)
        i += 1

    return blank_string

def solve_part_two(size, input):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
