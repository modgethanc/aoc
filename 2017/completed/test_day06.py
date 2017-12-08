#!/usr/bin/python3

"""
Testing module for day 6.
"""

import unittest
from shortcuts import *
from day06 import *

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    inputfile = open("day06-sample.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    inputs = intify(inputs[0].split())

    def test_find_most(self):
        self.assertEqual(find_most(self.inputs), 2)

    def test_one_redistribute(self):
        test_bank = self.inputs[:]
        result = redistribute(test_bank, find_most(test_bank))
        self.assertEqual(result, [2, 4, 1, 2])

    def test_example_one(self):
        self.assertEqual(solve_part_one(self.inputs), 5)
    '''
    def test_wrong(self):
        self.assertGreater(solve_part_one(inputs), 344)
    '''

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """

    inputfile = open("day06-sample.txt", 'r')
    inputs = []
    for line in inputfile:
        inputs.append(line)
    inputfile.close()

    inputs = intify(inputs[0].split())

    def test_example_one(self):
        self.assertEqual(find_final_state(self.inputs), [2,4,1,2])

    '''
    def test_wrong(self):
        self.assertGreater(solve_part_one(inputs), 344)
    '''

if __name__ == '__main__':
    unittest.main()
