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

    sampletree = make_tree(sample)
    #print(sampletree)
    #print(tower_weights("tknk", sampletree))

    def test_example_one(self):
        self.assertEqual(solve_part_two(self.sample), 60)

    def test_get_weight(self):
        self.assertEqual(get_weight("fwft (72) -> ktlj, cntj, xhth"), 72)

    def test_sum_weights(self):
        self.assertEqual(sum_weights("ugml", self.sampletree), 251)

    def test_sum_weights_two(self):
        self.assertEqual(sum_weights("padx", self.sampletree), 243)
    
    def test_find_culprits(self):
        self.assertEqual(find_culprit(tower_weights("tknk", self.sampletree)), ("ugml", 243))
    
    '''
    def test_balance_checker(self):
        self.assertTrue(is_balanced("padx", self.sampletree))
    
    def test_balance_checker_false(self):
        self.assertFalse(is_balanced("tknk", self.sampletree))
    def test_wrong(self):
        self.assertGreater(solve_part_one(self.inputs), 344)
    '''

if __name__ == '__main__':
    unittest.main()
