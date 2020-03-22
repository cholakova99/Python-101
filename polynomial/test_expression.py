import unittest
from expression import Expression

class TestPolynomial(unittest.TestCase):
	def test_wrong_input(self):
		expression = "6*x*x*x"
		exc = None
		try:
			res = Expression(expression)
		except ValueError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_not_string_is_given(self):
		expression = []
		exc = None
		try:
			res = Expression(expression)
		except AssertionError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_calculation_when_we_do_not_have_x(self):
		ex = "62"
		expression = Expression(ex)
		expected = "0"
		self.assertEqual(expected,expression.result)

	def test_calculation_when_we_have_no_coef(self):
		expression1 = Expression("x^6")
		expression2 = Expression("x")
		self.assertEqual(expression1.result,"6*x^5")
		self.assertEqual(expression2.result,"1")

	def test_calculation_when_we_have_coef(self):
		expression1 = Expression("6*x")
		expression2 = Expression("7*x^2")
		expression3 = Expression("2*x^0")
		self.assertEqual(expression1.result,"6")
		self.assertEqual(expression2.result,"14*x")
		self.assertEqual(expression3.result,"0")

	def test_with_no_degree(self):
		expression1 = Expression("x")
		expression2 = Expression("3*x")
		expression3 = Expression("3x")
		self.assertEqual(expression3.result,"3")
		self.assertEqual(expression2.result,"3")
		self.assertEqual(expression1.result,"1")

		
if __name__ == '__main__':
	unittest.main()
