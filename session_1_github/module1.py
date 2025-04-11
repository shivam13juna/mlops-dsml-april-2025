def greet(name):
	print(f"Hello, {name}!")

def main():
	user_name = "User"  # Dummy user name for demonstration
	greet(user_name)

if __name__ == '__main__':
	main()

# we use name == 'main' to ensure that the main function is called only when this script is run directly, not when imported as a module.