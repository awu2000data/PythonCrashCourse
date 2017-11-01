def greet_user(first_name, last_name):
	"""This is the docstring for this function"""
	formatted_name = get_formatted_name(first_name, last_name)
	print("Hello, " + formatted_name.title() + "!")


def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatle formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()



while True:
	print("\nEnter 'q' to quit")
	first_name = input("What is your first name: ")
	if first_name == 'q':
		break
	last_name = input("What is your last name: ")
	if last_name == 'q':
		break
	greet_user(first_name, last_name)