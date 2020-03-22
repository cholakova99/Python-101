import unittest
from utls import UTLS

class TestUTLS(unittest.TestCase):
	def test_utls_structure_another_letter(self):
		exp = None
		expr = "1*x^2+2x+5+6r"
		try:
			expression = UTLS(expr)
		except ValueError as error:
			exp = error
		self.assertIsNotNone(exp)

	def test_utls_structure_another_symbol(self):
		exp = None
		expr = "1+2x+5+6%"
		try:
			expression = UTLS(expr)
		except ValueError as error:
			exp = error
		self.assertIsNotNone(exp)

	def test_utls_structure_with_minus(self):
		exp = None
		expr = "1*x^2+2x+5-6"
		try:
			expression = UTLS(expr)
		except ValueError as error:
			exp = error
		self.assertIsNotNone(exp)

	def test_correct_utls_structure(self):
		exp = None
		expr = "2x^3 + 3x + 1"
		expected = ["2x^3","3x","1"]
		try:
			expression = UTLS(expr)
		except ValueError as error:
			exp = error
		self.assertIsNone(exp)
		self.assertEqual(expression.list_of_expressions,expected)








if __name__ == '__main__':
	unittest.main()
