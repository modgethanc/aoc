#!/usr/bin/python3

"""
Testing module for day x.
"""

import unittest
from dayx import solve_part_one
from dayx import solve_part_two

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("dayxx-sample.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one(inputs), 18)

    def test_wrong(self):
        self.assertGreater(solve_part_one(inputs), 344)

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """

    inputfile = open("dayxx-sample.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one(inputs), 18)

    def test_wrong(self):
        self.assertGreater(solve_part_one(inputs), 344)

if __name__ == '__main__':
    unittest.main()
