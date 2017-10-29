requested_toppings = []


if requested_toppings:
	for topping in requested_toppings:
		if topping == 'green peppers':
			print("Sorry we are out of " + topping)
		else:
			print("Adding " + topping)
	print("\n")
	print("Finished making your pizza")

else:
	print("Are you sure you want a plain pizza?")