from utls import UTLS 

class Expression:
	result = ""

	def validate_expression(self):
		times_met = 0
		for i in range(0,len(self.expression)):
			if self.expression[i] == 'x':
				times_met+=1
		if times_met != 0 and times_met != 1:
			return False
		return True


	def calculate_derivative(self):
		if 'x' not in self.expression:
			return "0"
		self.expression = self.expression.replace("^","")
		self.expression = self.expression.replace("*","")
		if self.expression[0] == 'x':
			array_helper = self.expression.split("x")
			array_helper = array_helper[1::]
			if len(self.expression)==1:
					return "1"
			else:
				times_multi = int(array_helper[0]) - 1
				result = array_helper[0] + "*" + "x" + "^" + str(times_multi)
		else:
			array_helper = self.expression.split("x")
			if array_helper[1] == "":
				return array_helper[0]
			if array_helper[1] == "1":
				return array_helper[0]
			if array_helper[1] == "0":
				return "0"
			if array_helper[1] == "2":
				return str(int(array_helper[0]) * int(array_helper[1])) + "*" + "x"
			else:
				result = str(int(array_helper[0]) * int(array_helper[1])) + "*" + "x" + "^" + str(int(array_helper[1]) - 1)
		return result

	
	
	def __init__(self,expression):
		if type(expression) is not str:
			raise AssertionError('Only strings are allowed')
		self.expression = expression
		if self.validate_expression() is False:
			raise ValueError('Expression was not given in the correct way')
		self.result = self.calculate_derivative()
