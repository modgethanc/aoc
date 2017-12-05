#!/usr/bin/python3

"""
AOC 2017 Day 5:
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
    print("part two solution: " + str(solve_part_two(inputs)))

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

    while index  in range(0, len(inputs)):
        JUMPS += 1
        movement = int(inputs[index])
        inputs[index] += 1
        index = index + movement

    return JUMPS

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    global JUMPS
    JUMPS = 0

    JUMPS = run_jumps_two(inputs)
    print(JUMPS)
    return JUMPS

def run_jumps_two(inputs):
    """
    """

    global JUMPS

    print(JUMPS)
    index = 0

    while index in range(0, len(inputs)):
        JUMPS += 1
        movement = int(inputs[index])
        if movement >= 3:
            inputs[index] -= 1
        else:
            inputs[index] += 1
        index = index + movement

    return JUMPS

if __name__ == '__main__':
    sys.exit(main())
