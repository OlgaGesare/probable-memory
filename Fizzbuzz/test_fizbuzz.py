import unittest
#import fizzbuzz
from fizzbuzz import fizz_buzz


class FizzBuzzTest(unittest.TestCase):
	"""Testing fizzbuzz
	"""

	def test_returns_fizz_when_passed_a_number_divisible_by_three(self):
		"""Test retuurn fizz when input is
		divisible by three 
		"""
		self.assertEqual(fizz_buzz(3), 'fizz')

	def test_returns_buzz_when_passed_a_number_divisible_by_five(self):
		"""Test retuurn buzz when input is
		divisible by five 
		"""
		self.assertEqual(fizz_buzz(5), 'buzz')

	def test_returns_fizbuzz_when_passed_a_number_divisible_by_three_and_five(self):
		"""Test retuurn fizzbuzz when input is
		divisible by three and five 
		"""
		self.assertEqual(fizz_buzz(15), 'fizzbuzz')