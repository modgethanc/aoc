#!/usr/bin/python3

"""
Testing module for day 5.
"""

import unittest
from day05 import solve_part_one
from day05 import solve_part_two

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    def test_example_one(self):
        inputfile = open("day05-sample.txt", 'r')
        inputs = []
        for line in inputfile:
            inputs.append(int(line.rstrip()))
        inputfile.close()

        self.assertEqual(solve_part_one(inputs), 5)

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """

    def test_example_one(self):
        inputfile = open("day05-sample.txt", 'r')
        inputs = []
        for line in inputfile:
            inputs.append(int(line.rstrip()))
        inputfile.close()

        self.assertEqual(solve_part_two(inputs), 10)

    def test_wrong_two(self):
        inputfile = open("day05-input.txt", 'r')
        inputs = []
        for line in inputfile:
            inputs.append(int(line))
        inputfile.close()
        ans = solve_part_two(inputs)
        self.assertNotEqual(ans, 261)

if __name__ == '__main__':
    unittest.main()
