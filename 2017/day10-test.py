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
'''
    def test_wrong(self):
        self.assertNotEqual(solve_part_one(256, self.inputs[0]), 60762)

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

    def test_example_one(self):
        self.assertEqual(solve_part_two(self.sample), 18)

    def test_wrong(self):
        self.assertGreater(solve_part_two(self.input), 344)
'''
if __name__ == '__main__':
    unittest.main()
