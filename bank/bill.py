class Bill:
	def __init__(self,amount):
		if type(amount) is not int:
			raise AssertionError('Type of the amount must be int')
		self.amount = amount

	def __str__(self):
		return f'A {self.amount}$ bill'

	def __repr__(self):
		return f'Bill {self}'

	def __int__(self):
		return self.amount

	def __eq__(self,other):
		if self.amount == other.amount:
			return True
		return False

	def __hash__(self):
		return hash(self.amount)