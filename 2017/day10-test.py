#!/usr/bin/python3

"""
Testing module for day x.
"""

import unittest
from day10 import *

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day10-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one(5, "3,4,1,5"), 12)

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """

    inputfile = open("day10-sample.txt", 'r')
    sample = []
    for line in inputfile:
        sample.append(line)
    inputfile.close()

    inputfile = open("day10-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    def test_converter(self):
        self.assertEqual(convert_sequence("1,2,3"), [49,44,50,44,51])

    def test_part_two(self):
        self.assertEqual(solve_part_two(256, ""), "a2582a3a0e66e6e86e3812dcb672a272")

    def test_part_two_two(self):
        self.assertEqual(solve_part_two(256, "AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")

    def test_part_two_three(self):
        self.assertEqual(solve_part_two(256, "1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")

    def test_part_two_four(self):
        self.assertEqual(solve_part_two(256, "1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

if __name__ == '__main__':
    unittest.main()
