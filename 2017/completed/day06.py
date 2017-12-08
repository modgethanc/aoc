#!/usr/bin/python3

"""
AOC 2017 Day 6:
    pretty easy cruise! i got to think carefully about how to break this up
    into individual steps for testing.
"""

import sys
from shortcuts import intify

def main():
    """
    Main entry point.
    """

    inputfile = open(sys.argv[1], 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    inputs = intify(inputs[0].split())

    print("part one solution: " + str(solve_part_one(inputs[:])))
    print("part two solution: " + str(solve_part_two(inputs[:])))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    solution = 0

    banks = inputs[:]
    states = [banks[:]]

    #print("starting: "+str(banks))

    while 1:
        solution += 1
        #print("step: "+str(solution))
        banks = redistribute(banks, find_most(banks))
        #print(banks, states)
        if banks in states:
            return solution
        else:
            states.append(banks[:])

def find_most(banks):
    """
    Finds the bank with the most blocks and returns its index. If there's a
    tie, go to the lowest index.
    """

    most = sorted(banks)[-1]
    #print("most: "+most)

    for index,bank in enumerate(banks):
     #   print("checking "+str(index))
        if bank == most:
      #      print("found")
            return index

def redistribute(banks, index):
    """
    Takes the blocks from the indexed bank and returns a redistributed array.
    """

    buffer = banks[index]
    banks[index] = 0

    while buffer > 0:
        buffer -= 1
        index = (index+1)%len(banks)
        banks[index] += 1

    return banks

def solve_part_two(inputs):
    """
    Solver for part two.
    """

    new_state = find_final_state(inputs)

    return solve_part_one(new_state)

def find_final_state(input_banks):
    """
    Returns the state this memory bank ends on.
    """

    banks = input_banks[:]
    states = [banks[:]]

    #print("starting: "+str(banks))

    while 1:
        #print("step: "+str(solution))
        banks = redistribute(banks, find_most(banks))
        #print(banks, states)
        if banks in states:
            return banks
        else:
            states.append(banks[:])


if __name__ == '__main__':
    sys.exit(main())
