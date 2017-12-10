#!/usr/bin/python3

"""
Testing module for day 9.
"""

import unittest
from day09 import *

class Day9TestCases(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day09-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve("{{{},{},{{}}}}")[0], 16)
    def test_example_two(self):
        self.assertEqual(solve("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0],9)
    def test_example_three(self):
        self.assertEqual(solve("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0],9)
    def test_example_four(self):
        self.assertEqual(solve("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0],3)
    def test_part_two(self):
        self.assertEqual(solve("<random characters>")[1], 17)
    def test_part_two_example_two(self):
        self.assertEqual(solve('<{o"i!a,<{i<a>')[1], 10)

if __name__ == '__main__':
    unittest.main()
