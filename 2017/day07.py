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

    print("part one solution: " + str(solve_part_one(inputs)))
    #print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    children = get_all_children(inputs)
    bases = get_all_bases(inputs)

    return list(set(bases).difference(set(children)))[0]

def get_base(line):
    """
    Given a single line from the input, return its base element.
    """

    return line.split(" ")[0]

def get_children(line):
    """
    Given a single line from the input, return a string list of its children.
    This should be empty if it has no children.
    """

    linesplit = line.split(" -> ")
    if len(linesplit) > 1:
        return linesplit[1].split(", ")
    else:
        return []

def get_all_children(inputs):
    """
    Given a full set of inputs, return a string list containing all unique
    children.
    """

    items = []

    for line in inputs:
        items.extend(get_children(line))

    return set(items)

def get_all_bases(inputs):
    """
    Given a full set of inputs, return a string list containing all unique
    bases.
    """

    items = []

    for line in inputs:
        items.append(get_base(line))

    return set(items)

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
