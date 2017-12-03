#!/usr/bin/python3

"""
AOC 2017 Day 2:
    thumbtyped miraculously under the covers; misinterpreted the input
    thinking i had whitespace woes from copy/paste, but actually it was
    weird python max/min behavior on input types
"""

import sys
def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    input = []
    for line in inputfile:
        input.append(line)
    inputfile.close()

    print("part one solution: " + str(solve_part_one(input)))
    print("part two solution: " + str(solve_part_two(input)))

    return 0

def solve_part_one(input):
    """
    Solver for part one.
    """

    solution = 0

    for line in input:
        eval = line.split()
        for index,item in enumerate(eval):
            eval[index] = int(item)
        solution += max(eval) - min(eval)

    return solution

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0

    for line in input:
        eval = line.split()
        for index,item in enumerate(eval):
            eval[index] = int(item)

        for item in eval:
            for check in eval:
                if item == check:
                    pass
                elif item % check == 0:
                    solution += item // check
    return solution

if __name__ == '__main__':
    sys.exit(main())
