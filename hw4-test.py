#!/usr/bin/python3

# student test file for HW3
import unittest
from hw4 import *
import string

class tester_most_common_char(unittest.TestCase):
    def test__given(self):
        self.assertEqual(most_common_char("aaaaabcde"), 'a')
        self.assertEqual(most_common_char("AAAbCDeeEE"), 'A')

class tester_alphabet_finder(unittest.TestCase):
    def test__given(self):
        self.assertEqual(alphabet_finder('abcdefghijklmnopqrstuvwxyzaaa'), string.ascii_lowercase)
        self.assertEqual(alphabet_finder('The quick brown fox jumps over the lazy doooooooooooooogoooooooo'), 'The quick brown fox jumps over the lazy doooooooooooooog')

class tester_string_my_one_true_love(unittest.TestCase):
    def test__given(self):
        self.assertTrue(string_my_one_true_love('aaabbbcccddde'))

class tester_alive_people(unittest.TestCase):
    def test__given(self):
        self.assertEqual(alive_people([[1920,80],[1940,22],[1961,10]]), 1961)

class tester_three_sum(unittest.TestCase):
    def test__given(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,4],0), [[-1,-1,2],[-1,0,1]])

class tester_happy_numbers(unittest.TestCase):
    def test__given(self):
        self.assertEqual(happy_numbers(8), 2)

if __name__ == "__main__":
	unittest.main(module=__name__, buffer=True, exit=False)
