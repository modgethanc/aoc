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

    print("part one solution: " + str(solve_part_one(inputs[0])))
    #print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    solution = 0

    steps = inputs.split(",")
    n = []
    s = []
    nw = []
    ne = []
    se = []
    sw = []

    for step in steps:
        if step == "n":
            n.append(step)
        elif step == "s":
            s.append(step)
        elif step == "nw":
            nw.append(step)
        elif step == "ne":
            ne.append(step)
        elif step == "sw":
            sw.append(step)
        elif step == "se":
            se.append(step)
    '''
    print("n:" + str(len(n)))
    print("s:" + str(len(s)))
    print("nw:" + str(len(nw)))
    print("ne:" + str(len(ne)))
    print("sw:" + str(len(sw)))
    print("se:" + str(len(se)))
    '''

    norths = len(n) - len(s)
    southeasts = len(se) - len(nw)
    northeasts = len(ne) - len(sw)

    print("norths: " + str(norths))
    print("southeasts: " + str(southeasts))
    print("northeasts: " + str(northeasts))

    return (norths - southeasts) + (northeasts + southeasts)

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
