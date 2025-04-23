a = 5
b = 10


def add_two_numbers(a, b):
	return a + b

def subtract_two_numbers(a, b):
	return a - b

def multiply_two_numbers(a, b):
	return a * b

def divide_two_numbers(a, b):
	if b == 0:
		return "Cannot divide by zero"
	else:
		return a / b