import unittest
from bill import Bill

class TestBill(unittest.TestCase):
	def test_not_integer_input_for_amount(self):
		exception = None
		amount = 34.6
		try:
			Bill(amount)
		except AssertionError as err:
			exception = err
		self.assertIsNotNone(exception)

	def test_string_for_input_for_amount(self):
		exception = None
		amount = "10"
		try:
			Bill(amount)
		except AssertionError as err:
			exception = err
		self.assertIsNotNone(exception)

	def test_equality(self):
		first = Bill(10)
		second = Bill(10)
		self.assertEqual(first,second)

	def test_not_equality(self):
		first = Bill(10)
		second = Bill(20)
		self.assertNotEqual(first,second)

	def test_str(self):
		example = Bill(10)
		expected_string = "A 10$ bill"
		self.assertEqual(expected_string,example.__str__())

	def test_int(self):
		example = Bill(10)
		self.assertEqual(int(example),10)


if __name__ == '__main__':
	unittest.main()