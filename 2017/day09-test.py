#!/usr/bin/python3

"""
Testing module for day 9.
"""

import unittest
from day09 import *

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day09-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one("{{{},{},{{}}}}"), 16)
    def test_example_two(self):
        self.assertEqual(solve_part_one("{{<!!>},{<!!>},{<!!>},{<!!>}}"),9)
    def test_example_three(self):
        self.assertEqual(solve_part_one("{{<!!>},{<!!>},{<!!>},{<!!>}}"),9)
    def test_example_four(self):
        self.assertEqual(solve_part_one("{{<a!>},{<a!>},{<a!>},{<ab>}}"),3)

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """
    '''
    inputfile = open("dayxx-sample.txt", 'r')
    sample = []
    for line in inputfile:
        sample.append(line)
    inputfile.close()

    inputfile = open("dayxx-input.txt", 'r')
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
