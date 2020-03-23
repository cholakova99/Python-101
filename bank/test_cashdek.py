import unittest
from cashdesk import CashDesk
from bill import Bill
from batch_bill import BatchBill

class TestCashDesk(unittest.TestCase):
	def test_take_money_that_are_not_bill_or_batchbill(self):
		exc = None
		money = 10
		desk = CashDesk()
		try:
			desk.take_money(money)
		except AssertionError as error:
			exc = error
		self.assertIsNotNone(exc)

	def test_take_money_that_are_Bill(self):
		exc = None
		money = Bill(10)
		desk = CashDesk()
		try:
			desk.take_money(money)
		except AssertionError as error:
			exc = error
		self.assertIsNone(exc)

	def test_take_monet_that_are_BatchBill(self):
		exc = None
		money = BatchBill([Bill(10),Bill(20)])
		desk = CashDesk()
		try:
			desk.take_money(money)
		except AssertionError as error:
			exc = error
		self.assertIsNone(exc)

	def test_total(self):
		desk = CashDesk()
		desk.take_money(Bill(15))
		desk.take_money(Bill(15))
		desk.take_money(BatchBill([Bill(15),Bill(25)]))
		self.assertEqual(70,desk.total())

	def test_inspect(self):
		desk = CashDesk()
		desk.take_money(Bill(15))
		desk.take_money(Bill(15))
		desk.take_money(BatchBill([Bill(15),Bill(25)]))
		expected = {'A 15$ bill': 3,'A 25$ bill': 1}
		self.assertEqual(expected,desk.inspect())

if __name__ == '__main__':
	unittest.main()

