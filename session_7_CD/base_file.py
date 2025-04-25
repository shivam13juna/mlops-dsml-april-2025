a = 5
b = 10
import pytest

# pytest fixture for connecting to a database
#@pytest.fixture
#def db_connection():
#	# Simulate a database connection
#	connection = "Database connection established"
#	yield connection
#	# Teardown code
#	connection = None
#	print("Database connection closed")


## use the fixture in a test
#def test_db_connection(db_connection):
#	assert db_connection == "Database connection established"


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