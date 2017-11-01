#Passing an arbitrary number of arguments

#optional arguments must come after positional/keyword
def make_pizza(size, *toppings):
	"""Print the list of toppings requested"""
	print("\nMaking a " + str(size) + " inch pizza with the following toppings")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'onion', 'pepperoni', 'ham')