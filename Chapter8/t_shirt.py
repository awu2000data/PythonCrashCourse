"""
Exercise 8-3
Write a function called make_shirt() that accepts
a size and a message that should be printed on the shirt.
The function should summarize the size and message.
Call the function once with positional and once
with keyword arguments.
"""

def make_shirt(size, message):
	print("\nThe " + size.upper() +
		" shirt will be printed with the following message: ")
	print(message)

make_shirt("l", "Positional Arguments")
make_shirt(size="m", message="Default Arguments")

