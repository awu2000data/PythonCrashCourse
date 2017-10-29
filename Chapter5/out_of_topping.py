requested_toppings = ['pepperoni', 'green peppers', 'mushroom', 'ham', 'chicken']

for topping in requested_toppings:
	if topping == 'green peppers':
		print("Sorry we are out of " + topping)
	else:
		print("Adding " + topping)
print("\n")
print("Finished making your pizza")