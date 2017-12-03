#!/usr/bin/python3

"""
Testing module for day 3.
"""

import unittest
from day03 import solve_part_one
from day03 import solve_part_two
from day03 import manhattan_distance
from day03 import gen_sequence

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    def test_example_one(self):
        self.assertEqual(solve_part_one(1), 0)

    def test_example_two(self):
        self.assertEqual(solve_part_one(12), 3)
    
    def test_example_three(self):
        self.assertEqual(solve_part_one(23), 2)
    
    def test_example_four(self):
        self.assertEqual(solve_part_one(1024), 31)

    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance((0,0), (1,2)), 3)
'''
    def test_wrong(self):
        input = open("day02input.txt", 'r')
        self.assertGreater(solve_part_one(input), 344)
        input.close()

    def test_wrong_two(self):
        input = open("day02input.txt", 'r')
        self.assertLess(solve_part_one(input), 61463)
        input.close()
        '''

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """
    def test_example_one(self):
        self.assertEqual(gen_sequence(1), 1)

    def test_example_two(self):
        self.assertEqual(gen_sequence(2), 1)
    
    def test_example_three(self):
        self.assertEqual(gen_sequence(3), 2)
    
    def test_example_four(self):
        self.assertEqual(gen_sequence(5), 5)
    
    def test_example_five(self):
        self.assertEqual(gen_sequence(13), 59)

if __name__ == '__main__':
    unittest.main()
