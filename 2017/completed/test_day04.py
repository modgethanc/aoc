#!/usr/bin/python3

"""
Testing module for day 4.
"""

import unittest
from day04 import validate
from day04 import validate_anagrams
from day04 import is_anagram

class PartOneTestCase(unittest.TestCase):
    """
    Tests for solve_part_one
    """

    def test_example_one(self):
        self.assertTrue(validate("aa bb cc dd ee"))

    def test_example_two(self):
        self.assertFalse(validate("aa bb cc dd aa"))

    def test_example_three(self):
        self.assertTrue(validate("aa bb cc dd aaa"))

class PartTwoTestCase(unittest.TestCase):
    """
    Tests for solve_part_two
    """

    def test_anagram_one(self):
        #print("test one")
        self.assertTrue(is_anagram("aba", "baa"))

    def test_anagram_two(self):
        #print("test two")
        self.assertFalse(is_anagram("aba", "baaa"))

    def test_anagram_three(self):
        #print("test three")
        self.assertFalse(is_anagram("aba", "aca"))

    def test_example_one(self):
        #print("validate one")
        self.assertTrue(validate_anagrams("abcde fghij"))

    def test_example_two(self):
        #print("validate two")
        self.assertFalse(validate_anagrams("abcde xyz ecdab"))

    def test_example_three(self):
        #print("validate three")
        self.assertTrue(validate_anagrams("a ab abc abd abf abj"))

    def test_example_four(self):
        #print("validate four")
        self.assertTrue(validate_anagrams("iiii oiii ooii oooi oooo"))

    def test_example_five(self):
        #print("validate five")
        self.assertFalse(validate_anagrams("oiii ioii iioi iiio"))

if __name__ == '__main__':
    unittest.main()
