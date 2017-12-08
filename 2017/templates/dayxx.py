#!/usr/bin/python3

"""
AOC 2017 Day :
"""

import sys
def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    print("part one solution: " + str(solve_part_one(inputs)))
    print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    solution = 0

    banks = inputs.split()

    return solution

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
