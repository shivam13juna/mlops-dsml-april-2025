from base_file import a, b, add_two_numbers, subtract_two_numbers, multiply_two_numbers, divide_two_numbers

#!pip install pytest


# Test the code

# pytest is a testing framework for Python that allows you to write simple and scalable test cases.


def test_a_functionality():

	assert add_two_numbers(2, 3) == 5, "Addition failed!"  # assert checks if the expression is True, if not it raises an AssertionError
	# assert checks if the expression is True, if not it raises an AssertionError


def test_b_functionality():

	assert subtract_two_numbers(5, 3) == 2, "Subtraction failed!"  # assert checks if the expression is True, if not it raises an AssertionError


def test_multiply_two_numbers():

	assert multiply_two_numbers(2, 3) == 6, "Multiplication failed!"  # assert checks if the expression is True, if not it raises an AssertionError

#if __name__ == "__main__":
#	# Run the tests
#	test_a_functionality()
#	test_b_functionality()
#	print("All tests passed!")