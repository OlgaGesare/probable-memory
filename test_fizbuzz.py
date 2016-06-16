import unittest
#import fizzbuzz
from fizzbuzz import fizz_buzz


class FizzBuzzTest(unittest.Testcase):
	"""Testing fizzbuzz
	"""

	def test_returns_fizz_when_passed_passed_a_number_divisible_by_three(self):
		"""Test return fizz when input is
		divisible by three 
		"""
		self.assertEqual(fizzbuzz.fizz_buzz(3), 'fizz')