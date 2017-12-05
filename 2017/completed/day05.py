#!/usr/bin/python3

"""
AOC 2017 Day 5:
    wow! i really enjoyed the fact that my brain immediately went to a
    recursive solution, but didn't anticipate recursion limits. learned
    something here :3

    the recursive version is saved in a different file for reference.
"""

import sys

def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(int(line))
    inputfile.close()

    print("part one solution: " + str(solve_part_one(inputs)))

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(int(line))
    inputfile.close()
    print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    jumps = 0
    index = 0

    while index in range(0, len(inputs)):
        jumps += 1
        movement = int(inputs[index])
        inputs[index] += 1
        index = index + movement

    return jumps

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    jumps = 0
    index = 0

    while index in range(0, len(inputs)):
        jumps += 1
        movement = int(inputs[index])
        if movement >= 3:
            inputs[index] -= 1
        else:
            inputs[index] += 1
        index = index + movement


    return jumps

if __name__ == '__main__':
    sys.exit(main())
