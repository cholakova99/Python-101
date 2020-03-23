from bill import Bill
class BatchBill:
	def all_elements_bills(self,list_of_bills):
		for i in range(0,len(list_of_bills)):
			if type(list_of_bills[i]) is not Bill:
				return False
			i+=1
		return True

	def __init__(self,list_of_bills):
		if type(list_of_bills) is not list:
			raise AssertionError('Type of list of bills must be list')
		if self.all_elements_bills(list_of_bills) is False:
			raise AssertionError('Only bills are allowed in the list!')
		self.list_of_bills = list_of_bills

	def __len__(self):
		return len(self.list_of_bills)

	def total(self):
		sum = 0
		for i in range(0,self.__len__()):
			sum = sum + self.list_of_bills[i].__int__()
		return sum

	def __getitem__(self,index):
		if index > self.__len__() - 1:
			return ValueError('There is not element with that index!')
		element = self.list_of_bills[index]
		return element

