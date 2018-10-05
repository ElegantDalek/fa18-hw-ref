#!/usr/bin/python3

# student test file for HW3
import unittest
from hw4 import *

class tester_most_common_char(unittest.TestCase):
    def test__given(self):
        self.assertEqual(most_common_char("aaaaabcde"), 'a')
        self.assertEqual(most_common_char("AAAbCDeeEE"), 'A')

#===================================
'''
class tester_matrix_multiply(unittest.TestCase):
	def test__given(self):
		self.assertEqual(matrix_multiply([[1,4,6]], [[2,3],[5,8],[7,9]]), [[64,89]])

class tester_nth_largest_element(unittest.TestCase):
	def test__given(self):
		self.assertEqual(nth_largest_element([3, 1, 5, 2, 4], 3), 3)
		self.assertEqual(nth_largest_element([-331, -776, 917, 399, -768, -183, -116, 278, -544, -669], 5), -183)
		self.assertEqual(nth_largest_element([-788, 227, 22, -204, 569, -650, -692, -319, 378, -297], 9), -692)

class tester_reverse_block(unittest.TestCase):
	def test__given(self):
		self.assertEqual(reverse_block([1,2,3, 4,5,6, 7], 3), [3,2,1, 6,5,4, 7])

class tester_subset_sum(unittest.TestCase):
	def test__given(self):
		self.assertTrue(subset_sum([1,2,3,4,5,7], 13))
		self.assertFalse(subset_sum([1,2,-1,5,4,-196], 196))

class tester_spiral_matrix(unittest.TestCase):
	def test__given(self):
		in_arr = \
		[[ 1, 2, 3, 4, 5],
		 [ 6, 7, 8, 9,10],
		 [11,12,13,14,15],
		 [16,17,18,19,20],
		 [21,22,23,24,25]]
		out_arr = [1,2,3,4,5, 10,15,20,25, 24,23,22,21, 16,11,6, 7,8,9, 14,19, 18,17, 12, 13]
		self.assertEqual(spiral_matrix(in_arr), out_arr)
'''
#===================================

if __name__ == "__main__":
	unittest.main(module=__name__, buffer=True, exit=False)
