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

    #print(input)

    x = 0
    y = 0

    square = 1
    i = 1
    move = -1
    dir_counter = 0
    step = 1

    while i < input:
        #print(str(i) + ": " + str((x,y)))

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

    #print((x,y))
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

def gen_sequence(max_square):
    """
    Generates part two sequence up to the given max square.

    scratched function: tried to generate the grid and index into it to find
    values, but oh god i'm sleepy

    value = 1

    grid = generate_grid(max_square+1)
    value_grid = { (0,0):1 }

    i = 0

    while i < max_square:

        i += 1
        value_grid.update({grid.get(i):value})

    print(value_grid)

    return value
    """

    ## CURRENT GOAL: try to brute-force this

    value = 1

    if max_square == 2:
        return value
    else:
        value_table = [0, 1, 1]
        n = 3
        while n <= max_square:
            # start with immediate predecessor
            value = value_table[n-1]

            # clean up
            value_table.append(value)
            n += 1

    print(value_table)

    return value

def generate_grid(max_square):
    """
    Return a dict of a grid of coordinates up to the max square.
    """

    grid = { 1:(0,0)}

    x = 0
    y = 0

    square = 1
    i = 1
    move = -1
    dir_counter = 0
    step = 1

    while i < max_square:
        #print(str(i) + ": " + str((x,y)))

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

        # cleanup
        step += 1
        i += 1
        grid.update({i:(x,y)})

    print(grid)

    return(grid)

if __name__ == '__main__':
    sys.exit(main())
