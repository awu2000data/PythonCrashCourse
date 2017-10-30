"""
Exercise 7-4
Write a loop that prompts the user to enter
a series of pizza toppings until they
enter 'quit'.  As they enter each topping
print a message saying that you'll add the
topping to the pizza
"""

prompt = "Enter a pizza topping('quit' to stop): "
active = True
while active:
	topping = input(prompt)
	if topping == 'quit':
		active = False
	else:
		print("Adding " + topping + " to your pizza")
		print("\n")