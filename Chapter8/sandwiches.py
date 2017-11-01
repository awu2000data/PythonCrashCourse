"""
Exercise 8-12
Write a function that accepts a list of items
that a person wants on a sandwich. The function
should have one parameter that takes as many
items as the call provides.  It should print
a summary of the sandwich being made. 
Call the function three times
"""

def make_sandwich(*items):
	if items:
		print("\nMaking a sandwich with the following items: ")
		for item in items:
			print('- ' + item)

make_sandwich('ham','turkey','cheddar cheese')
make_sandwich()
make_sandwich('roast beef', 'onions', 'swiss')
make_sandwich('bacon', 'lettuce', 'tomato')	