#!/usr/bin/python3

"""
AOC 2017 Day 1
"""

import sys

def main():
    """
    Main entry point.
    """

    print("part one solution: " + str(solve_part_one(sys.argv[1])))
    print("part two solution: " + str(solve_part_two(sys.argv[1])))

    return None

def solve_part_one(input):
    """
    Returns solution for given captcha for part one.
    """

    solution = 0
    inputList = list(input)

    for index,number in enumerate(inputList):
        if number == inputList[(index+1)%len(inputList)]:
            solution += int(number)

    return solution

def solve_part_two(input):
    """
    Returns solution for given captcha for part two.
    """

    solution = 0
    inputList = list(input)

    step = len(inputList)//2

    for index,number in enumerate(inputList):
        if number == inputList[(index+step)%len(inputList)]:
            solution += int(number)

    return solution

if __name__ == '__main__':
    sys.exit(main())
