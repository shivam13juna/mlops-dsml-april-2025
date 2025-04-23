from base_file import a, b, add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers


print(a, b, add_two_numbers(a, b), subtract_two_numbers(a, b), multiply_two_numbers(a, b), divide_two_numbers(a, b))
# Test the code

# pytest is a testing framework for Python that allows you to write simple and scalable test cases.


def test_c_functionality():

	assert multiply_two_numbers(2, 3) == 6
	# assert checks if the expression is True, if not it raises an AssertionError


def test_d_functionality():

	assert divide_two_numbers(6, 3) == 2


