available_toppings = ['mushrooms', 'olive', 'green peppers', 
						'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
	if topping in available_toppings:
		print("Adding " + topping)
	else:
		print("Sorry we are out of " + topping)		
print("\n")
print("Finished making your pizza")