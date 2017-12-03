#!/usr/bin/python3

"""
AOC 2017 Day 3:
"""

import sys
def main():
    """
    Main entry point.
    """
    """
    inputfile = open(sys.argv[1], 'r')
    input = []
    for line in inputfile:
        input.append(line)
    inputfile.close()
    """

    input = 361527

    print("part one solution: " + str(solve_part_one(input)))
    print("part two solution: " + str(solve_part_two(input)))

    return 0

def solve_part_one(input):
    """
    Solver for part one.
    """

    print(input)

    x = 0
    y = 0

    square = 1
    i = 1
    move = -1
    dir_counter = 0
    step = 1

    while i < input:
        print(str(i) + ": " + str((x,y)))

        turn = False

        if x == y:
            turn = True
            move *= -1
            dir_counter += 1
            step = 1
            y += move

        elif step <= dir_counter:
            y += move
        else:
            x += move

        step += 1
        i += 1

    print((x,y))
    return  manhattan_distance((0,0), (x,y))

def manhattan_distance(start, end):
    sx, sy = start
    ex, ey = end

    return abs(ex - sx) + abs(ey - sy)

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0

    return solution

if __name__ == '__main__':
    sys.exit(main())
