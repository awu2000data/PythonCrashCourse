toppings = ['pepperoni','olives','mushrooms','ham']
requested_topping = 'mushrooms'

print("Checking for inequality")
for topping in toppings:
	if topping != requested_topping:
		print(topping + " isn't the requested topping")
	else:
		print(topping + " is the requested topping")