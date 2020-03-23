from bill import Bill
from batch_bill import BatchBill 

class CashDesk:
	amount_of_money = 0
	list_of_bills_in_desk = []
	def __init__(self):
		pass
		# self.amount_of_money = amount_of_money
		# self.list_of_bills_in_desk = list_of_bills_in_desk

	def take_money(self,money):
		if type(money) is not Bill and type(money) is not BatchBill:
			raise AssertionError('You can only take money as Bill or BanchBill')
		if type(money) is Bill:
			self.amount_of_money = self.amount_of_money + money.__int__()
			
		if type(money) is BatchBill:
			for i in range(0,money.__len__()):
				self.amount_of_money = self.amount_of_money + money.__getitem__(i).__int__()
		self.list_of_bills_in_desk.append(money)


	def total(self):
		return self.amount_of_money

	def inspect(self):
		bills_dict = {}
		for i in range(0,len(self.list_of_bills_in_desk)):
			if type(self.list_of_bills_in_desk[i]) is Bill:
				if self.list_of_bills_in_desk[i].__str__() in bills_dict:
					bills_dict[self.list_of_bills_in_desk[i].__str__()] +=1
				else:
					bills_dict[self.list_of_bills_in_desk[i].__str__()] = 1
			if type(self.list_of_bills_in_desk[i]) is BatchBill:
				for j in range(0,self.list_of_bills_in_desk[i].__len__()):
					if self.list_of_bills_in_desk[i].__getitem__(j).__str__() in bills_dict:
						bills_dict[self.list_of_bills_in_desk[i].__getitem__(j).__str__()] +=1
					else:
						bills_dict[self.list_of_bills_in_desk[i].__getitem__(j).__str__()] = 1
		return bills_dict


