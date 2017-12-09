#!/usr/bin/python3

"""
Testing module for day x.
"""

import unittest
from day07 import *

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day07-sample.txt", 'r')
    sample = []
    for line in inputfile:
        sample.append(line.rstrip())
    inputfile.close()

    inputfile = open("day07-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one(self.sample), "tknk")

    def test_get_base(self):
        self.assertEqual(get_base("fwft (72) -> ktlj, cntj, xhth"), "fwft")

    def test_get_children(self):
        self.assertEqual(get_children("fwft (72) -> ktlj, cntj, xhth"), ["ktlj", "cntj", "xhth"])

    def test_correct_input_count(self):
        self.assertEqual(len(get_all_children(self.sample)), 12)

    def test_wrong(self):
        self.assertNotEqual(solve_part_one(self.inputs), "jkqnf")

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """
    '''

    inputfile = open("day07-sample.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    def test_example_one(self):
        self.assertEqual(solve_part_one(self.inputs), 18)

    def test_wrong(self):
        self.assertGreater(solve_part_one(self.inputs), 344)
    '''

if __name__ == '__main__':
    unittest.main()
