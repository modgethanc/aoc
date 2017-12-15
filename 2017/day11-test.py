#!/usr/bin/python3

"""
Testing module for day 11.
"""

import unittest
from day11 import *

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day11-input.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line.rstrip())
    inputfile.close()

    '''
    def test_example_one(self):
        self.assertEqual(solve_part_one("ne,ne,ne"), 3)

    def test_example_two(self):
        self.assertEqual(solve_part_one("ne,ne,sw,sw"), 0)
    '''

    def test_example_three(self):
        self.assertEqual(solve_part_one("ne,ne,s,s"), 2)

    '''
    def test_example_four(self):
        self.assertEqual(solve_part_one("se,sw,se,sw,sw"), 3)

    def test_my_exmaple_1(self):
        self.assertEqual(solve_part_one("n,n,n,n,se,se,ne,ne,ne"), 7)

    def test_my_exmaple_2(self):
        self.assertEqual(solve_part_one("n,n,n,n,n,ne,ne,ne,ne,se,se"), 9)

    def test_wrong_ans_1(self):
        self.assertLess(solve_part_one(self.inputs[0]), 686)

    def test_wrong_ans_2(self):
        self.assertGreater(solve_part_one(self.inputs[0]), 623)
    '''

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
