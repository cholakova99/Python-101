import sys
from utls import UTLS 
from expression import Expression


def calculate_expression(str):
	list_of_results = []
	result = ""
	helper = UTLS(str)
	for i in range(0,len(helper.list_of_expressions)):
			res = Expression(helper.list_of_expressions[i])
			list_of_results.append(res.result)
	for i in range(0,len(list_of_results)):
			result = result + "+" + list_of_results[i]
	result = result[1::]
	return result


def main():
	exp = sys.argv[1]
	result = calculate_expression(exp)
	print(result)

	
if __name__ == '__main__':
	main()
