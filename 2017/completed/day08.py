#!/usr/bin/python3

"""
AOC 2017 Day 8:
    10% thumbtyped other than starter code template from previous days! i
    enjoyed forcing myself to find a balance between brevity and
    expressiveness.

    making use of tuples and such is very helpful lately.
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

    (solution1, solution2) = solve(inputs)

    print("part one solution: " + str(solution1))
    print("part two solution: " + str(solution2))

    return 0

def solve(inputs):
    """
    Solver for both parts, returned as a tuple.
    """

    registers = {}
    value_history= []

    for line in inputs:
        (registers, value_history) = update_registers(line, registers, value_history)

    return sorted(registers.values())[-1], sorted(value_history)[-1]

def update_registers(line, registers, value_history):
    """
    Given a input line, make the modification based on the register dict.
    """

    if evaluate(line, registers):
        (register, modification, value) = line.split()[0:3]
        value = int(value)
        item = registers.get(register, 0)

        if modification == "inc":
            new_value = item + value
            registers.update({register:new_value})
        else:
            new_value = item - value
            registers.update({register:new_value})

        value_history.append(new_value)

    return registers, value_history

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

if __name__ == '__main__':
    sys.exit(main())
