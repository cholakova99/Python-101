import unittest
from fractions_dis import Fraction, ListFraction

class TestFraction(unittest.TestCase):
	def test_cannot_instantiate_fraction_with_zero_denominator(self):
		exception = None

		try:
			Fraction(1,0)
		except AssertionError as exc:
			exception = exc 
		self.assertIsNotNone(exception)

	def test_fraction_string_representation_is_as_expected_one(self):
		fraction1 = Fraction(1,3)
		fraction2 = Fraction(-1,3)
		fraction3 = Fraction(2,4)

		self.assertEqual(str(fraction1),'1/3')
		self.assertEqual(str(fraction2),'-1/3')
		self.assertEqual(str(fraction3),'2/4')

	def test_fraction_equalization_with_equal_fractions(self):
		fraction1 = Fraction(1,5)
		fraction2 = Fraction(1,5)
		self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

	def test_simplified_fraction_is_preserved_after_simplification(self):
		fraction = Fraction(1,5)
		expected = Fraction(1,5)
		self.assertEqual(fraction.simplify(),expected)

	def test_fraction_is_simplified_as_expected(self):
		fraction = Fraction(2,10)
		expected = Fraction(1,5)
		self.assertEqual(fraction.simplify(),expected)

	def test_assition_fractions_works_correct_for_non_simplifiable_result(self):
		fraction1 = Fraction(1,6)
		fraction2 = Fraction(2,7)
		result = fraction1 + fraction2
		self.assertEqual(result.numerator, 19)
		self.assertEqual(result.denumerator, 42)

	def test_all_types_in_list(self):
		exc = None 
		try:
			ListFraction([Fraction(1,3),Fraction(2,3),8]).collect()
		except AssertionError as err:
			exc = err
		self.assertIsNotNone(exc)

	def test_one_fraction_in_list(self):
		my_list_fractions = [Fraction(1,3)]
		my_list = ListFraction(my_list_fractions)
		expected = Fraction(1,3)
		self.assertEqual(my_list.collect(),expected)

	def test_collect_fractions_from_list_with_more_than_one_fractions(self):
		my_list = ListFraction([Fraction(1,7),Fraction(2,6)])
		expected = Fraction(10,21)
		self.assertEqual(my_list.collect(),expected)

	def test_collect_fractions_from_list_with_more_than_two_fractions(self):
		my_list = ListFraction([Fraction(1,5),Fraction(1,5),Fraction(2,5)])
		expected = Fraction(4,5)
		self.assertEqual(my_list.collect(),expected)

	def test_sort_list(self):
		my_list = ListFraction([Fraction(2,3),Fraction(1,3)])
		my_list_2 = ListFraction([Fraction(5, 6), Fraction(22, 78), Fraction(22, 7), Fraction(7, 8), Fraction(9, 6), Fraction(15, 32)])
		expected = [Fraction(1,3),Fraction(2,3)]
		expected2 = [Fraction(22, 78), Fraction(15, 32), Fraction(5, 6), Fraction(7, 8), Fraction(9, 6), Fraction(22, 7)]
		self.assertEqual(my_list.sort_fractions(),expected)
		self.assertEqual(my_list_2.sort_fractions(),expected2)
	

if __name__ == '__main__':
	unittest.main()
