
class UTLS:
	def convert_to_correct_form(self,expression):
		if type(expression) is not str:
			raise AssertionError
		not_forbidden_signs = ["^"," ","1","2","3","4","5","6","7","8","9","0","x","*","/"]
		for i in range(0,len(expression)):
			if expression[i] not in not_forbidden_signs:
				raise ValueError('Fobidden sign was used!')
			else:
				i+=1
		return True




	list_of_expressions = []

	def __init__(self,strn):
		if type(strn) is not str:
			raise AssertionError('Not-string argument')
		strn = strn.replace(" ","")
		helper = strn.split('+')
		for i in range(0,len(helper)):
			if self.convert_to_correct_form(helper[i]) is True:
				i+=1
		self.list_of_expressions =  helper

	def __eq__(self,other):
		if len(self.list_of_expressions) != len(other.list_of_expressions):
			return False
		for i in range(0,len(self.list_of_expressions)):
			if self.list_of_expressions[i] == other.list_of_expressions[i]:
				i+=1
			else:
				return False
		return True

	



