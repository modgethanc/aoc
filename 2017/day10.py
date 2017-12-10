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


    #print("part one solution: " + str(solve_part_one(256, inputs[0])))
    print("part two solution: " + str(solve_part_two(256, inputs[0])))

    return 0

def solve_part_one(size, inputs):
    """
    Solver for part one.
    """

    sequence = intify(inputs.split(","))

    knot = make_string(size)
    tie_knot(knot, 0, 0, sequence)

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

def tie_knot(knot, position, skip, sequence):
    """
    Given a knot, position, skip, and sequence, perform all the knot-tying
    steps and return the current knotstring, position, and skip.
    """

    #print("starting: "+str(knot))

    size = len(knot)

    for length in sequence:
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

    return knot, position, skip

def solve_part_two(size, inputs):
    """
    Solver for part two.
    """

    solution = ""

    # wrangle sequence
    tail = intify("17, 31, 73, 47, 23".split(","))
    sequence = convert_sequence(inputs)
    sequence.extend(tail)

    # run 64 rounds
    i = 0
    knot = make_string(size)
    skip = 0
    position = 0
    while i < 64:
        (knot, position, skip) = tie_knot(knot, position, skip, sequence)
        i += 1

    # create dense hash
    dense = []
    block = 0
    i = 0
    while i < size:
        block ^= knot[i]
        i += 1
        if (i % 16) == 0:
           dense.append(block) 
           block = 0

    for item in dense:
        converted = hex(item)
        padding = ""
        if len(converted) < 4:
            padding = "0"
        solution += padding + converted[2:]

    return solution

def convert_sequence(raw_seq):
    """
    Given a raw string, convert it to a list of the ascii codes.
    """

    codes = []

    for item in list(raw_seq):
        codes.append(ord(item))

    return codes

if __name__ == '__main__':
    sys.exit(main())
