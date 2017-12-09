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
    print("part two solution: " + str(solve_part_two(inputs)))

    return 0

def solve_part_one(inputs):
    """
    Solver for part one.
    """

    registers = {}

    for line in inputs:
        registers = update_registers(line, registers)

    return sorted(registers.values())[-1]

def update_registers(line, registers):
    """
    Given a input line, make the modification based on the register dict.
    """

    if evaluate(line, registers):
        (register, modification, value) = line.split()[0:3]
        value = int(value)
        item = registers.get(register, 0)

        if modification == "inc":
            registers.update({register:item+value})
        else:
            registers.update({register:item-value})

    return registers

def evaluate(line, registers):
    """
    Given a line of instructions, parse and evuluate it with respect to the
    register dict.
    """

    (item, operator, target) = line.split()[4:]
    target = int(target)
    value = registers.get(item, 0)

    if operator == "<":
        return value < target
    elif operator == ">":
        return value > target
    elif operator == "==":
        return value == target
    elif operator == "<=":
        return value <= target
    elif operator == ">=":
        return value >= target
    elif operator == "!=":
        return value != target

def solve_part_two(input):
    """
    Solver for part two.
    """

    solution = 0



    return solution

if __name__ == '__main__':
    sys.exit(main())
