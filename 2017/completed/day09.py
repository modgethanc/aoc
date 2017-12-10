#!/usr/bin/python3

"""
AOC 2017 Day 9:
    -pretty breezy string parser
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

    (part1, part2) = solve(inputs[0])

    print("part one solution: " + str(part1))
    print("part two solution: " + str(part2))

    return 0

def solve(inputs):
    """
    Solver for part one.
    """

    solution = 0
    score = 0
    removed = 0
    skip = False
    garbage = False

    for item in list(inputs):
        if skip:
            skip = False
            continue

        if item == "!":
            skip = True
            continue


        if garbage:
            if item == ">":
                garbage = False
            else:
                removed += 1
            continue

        if item == "<":
            garbage = True
            continue

        if item == "{":
            score += 1
            solution += score
        elif item == "}":
            score -= 1

    return solution, removed

if __name__ == '__main__':
    sys.exit(main())
