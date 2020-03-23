import unittest
from batch_bill import BatchBill
from bill import Bill

class TestBatchBill(unittest.TestCase):
	def test_not_all_elements_are_bills(self):
		exc = None
		list_of_elements = [Bill(10),Bill(10),20]
		try:
			BatchBill(list_of_elements)
		except AssertionError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_all_elements_are_bills(self):
		exc =None
		list_of_elements = [Bill(10),Bill(20)]
		try:
			BatchBill(list_of_elements)
		except AssertionError as error:
			exc = error
		self.assertIsNone(exc)

	def test_total(self):
		list_of_elements = [Bill(14),Bill(17),Bill(12)]
		self.assertEqual(43,BatchBill(list_of_elements).total())

	def test_get_item(self):
		first_item = Bill(14)
		second_item = Bill(15)
		list_of_elements = [first_item,second_item]
		batch = BatchBill(list_of_elements)
		self.assertEqual(second_item,batch.__getitem__(1))

	def test_len(self):
		first_item = Bill(14)
		second_item = Bill(15)
		list_of_elements = [first_item,second_item]
		batch = BatchBill(list_of_elements)
		self.assertEqual(2,batch.__len__())




if __name__ == '__main__':
	unittest.main()