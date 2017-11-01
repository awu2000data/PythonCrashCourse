"""
Exercise 8-14
Write a function that stores information about
a car in a dictionary.  The function should
always receive a manufacturer and a model name.
It should then accept an arbitrary number of 
keyword arguments.  Call the function with
the require information and three other k/v pairs.
Print the returned dictionary
"""

def define_car(manufacturer, model, **features):
	car = {}
	car['manufacturer'] = manufacturer
	car['model'] = model
	for key, value in features.items():
		car[key] = value
	return car

car = define_car('dodge', 'neon', color='silver',
				year='2005', wheels='four')
print(car)