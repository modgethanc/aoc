#!/usr/bin/python3

"""
AOC 2017 Day 5:
    the recursive solution for part 1, which works on a test but runs into recursion limit on the entry.
"""

import sys

JUMPS = 0

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
#    print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    global JUMPS
    JUMPS = 0

    return run_jumps(inputs, 0)

def run_jumps(inputs, index):
    """
    """

    global JUMPS

    print(JUMPS)
    while index not in range(0, len(inputs)):
        return JUMPS

    JUMPS += 1
    movement = int(inputs[index])
    inputs[index] += 1

    return run_jumps(inputs, index + movement)

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0

    return solution

if __name__ == '__main__':
    sys.exit(main())
