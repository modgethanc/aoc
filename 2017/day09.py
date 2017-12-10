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
        inputs.append(line.rstrip())
    inputfile.close()

    print("part one solution: " + str(solve_part_one(inputs[0])))
    #print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    solution = 0
    score = 0
    skip = False
    garbage = False

    for item in list(inputs):
        if skip:
            skip = False
            continue

        if item == "!":
            skip = True
            continue
        elif item == "<":
            garbage = True
            continue

        if not garbage:
            if item == "{":
                score += 1
                solution += score
            elif item == "}":
                score -= 1
        elif item == ">":
            garbage = False

    return solution

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
