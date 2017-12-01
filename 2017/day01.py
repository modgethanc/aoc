#!/usr/bin/python3

"""
AOC 2017 Day 1
"""

import sys

def main():
    """
    Main entry point.
    """

    print("captcha solution: " + str(solve_captcha(sys.argv[1])))

    return None

def solve_captcha(input):
    """
    Returns solution for given captcha.
    """

    solution = 0
    inputList = list(input)

    #print("inputs:" + str(inputList))

    for index,number in enumerate(inputList):
        if number == inputList[(index+1)%4]:
            solution += int(number)

    return solution

if __name__ == '__main__':
    sys.exit(main())
