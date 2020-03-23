from math import gcd

class Fraction:
	def __init__(self,numerator,denumerator):
		if denumerator < 1:
			raise AssertionError('Zero or negative denominator.')
		self.numerator = numerator
		self.denumerator = denumerator


	def __str__(self):
		return f'{self.numerator}/{self.denumerator}'

	def simplify(self):
		devider = gcd (self.numerator,self.denumerator)
		return Fraction(self.numerator // devider , self.denumerator // devider)

	def __repr__(self):
		return f'Fraction {self}'

	def __gt__(self,other):
		if self.numerator * other.denumerator > other.numerator * self.denumerator:
			return True
		else:
			return False

	def __eq__(self, other):
		return self.numerator/self.denumerator == other.numerator/other.denumerator

	def __add__(self,other):
		numerator = (self.numerator * other.denumerator) + (other.numerator * self.denumerator)
		denumerator = self.denumerator * other.denumerator
		return Fraction(numerator,denumerator)

	

class ListFraction:

	def all_elements_of_list_are_fractions(self,list_fractions):
		for i in range(0,len(list_fractions)):
			if type(list_fractions[i]) is Fraction:
				i+=1
			else:
				return False
		return True

	def __eq__(self,other):
		if len(self.list_fractions) != len(other.list_fractions):
			return False
		else:
			for i in range(0,len(self.list_fractions)):
				if self.list_fractions[i].__eq__(other.list_fractions):
					i+=1
				else:
					return False
		return True




	def __init__(self,list_fractions):
		if self.all_elements_of_list_are_fractions(list_fractions) is False:
			raise AssertionError('Not all elements are fractions!')
		self.list_fractions = list_fractions


	def collect(self):
		if type(self.list_fractions) is list:
			if self.all_elements_of_list_are_fractions(self.list_fractions):
				if len(self.list_fractions) == 0:
					return ()
				if len(self.list_fractions) == 1:
					return self.list_fractions[0]
				else:
					sum = Fraction(0,1)
					for i in range(0,len(self.list_fractions)):
						sum = sum.__add__(self.list_fractions[i])
					return sum

	def sort_fractions(self,ascending=True):
		for i in range(0,len(self.list_fractions)-1):
			for j in range(i+1,len(self.list_fractions)):
				if self.list_fractions[i].__gt__(self.list_fractions[j]):
					tmp = self.list_fractions[i]
					self.list_fractions[i] = self.list_fractions[j]
					self.list_fractions[j] = tmp
		if ascending is True:
			return self.list_fractions
		else:
			self.list_fractions = self.list_fractions[::-1]
			return self.list_fractions



		



