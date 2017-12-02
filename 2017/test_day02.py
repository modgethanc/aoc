#!/usr/bin/python3

"""
Testing module for day 1.
"""

import unittest
from day02 import solve_part_one
from day02 import solve_part_two

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    """
    def test_sample(self):
        self.assertEqual(solve_part_one("1111"), 0, 'this should fail')
    """

    def test_example_one(self):
        input = open("day02-sample.txt", 'r')
        self.assertEqual(solve_part_one(input), 18)

    def test_wrong(self):
        input = open("day02input.txt", 'r')
        self.assertGreater(solve_part_one(input), 344)

    def test_wrong_two(self):
        input = open("day02input.txt", 'r')
        self.assertLess(solve_part_one(input), 61463)
class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """
    def test_example_one(self):
        input = open("day02-sample2.txt", 'r')
        self.assertEqual(solve_part_two(input), 9)

"""
    def test_example_one(self):
        self.assertEqual(solve_part_two("1221"), 0)

    def test_example_one(self):
        self.assertEqual(solve_part_two("123425"), 4)

    def test_example_one(self):
        self.assertEqual(solve_part_two("123123"), 12)

    def test_example_one(self):
        self.assertEqual(solve_part_two("12131415"), 4)
        """

if __name__ == '__main__':
    unittest.main()
