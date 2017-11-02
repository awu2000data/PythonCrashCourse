"""
Exercise 9-4
Start with your 9-1 restaurant.py

Add an attr called number_served defaulted to 0
Create an instance and print the # of cust served.
Update the value then print the # again.

Add a method called set_number_served()
Call this method then print the # again

Add a method called increment_number_served()
Call it then print the # again
"""


class Restaurant():
	"""A simple representation of a restaurant"""

	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type"""
		self.name = name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print the name and what it serves"""
		print(self.name.title() + " serves " + self.cuisine_type + " food.")

	def open_restaurant(self):
		"""Alert that the restaurant is open"""
		print(self.name.title() + " is now open!")

	def set_number_served(self, served):
		"""Set the number of served guests to the specified amount"""
		self.number_served = served

	def increment_number_served(self, served):
		"""Increase the number of guests served by the passed in number"""
		self.number_served += served		


my_restaurant = Restaurant('casalinga', 'italian')
print("Customers served: " + str(my_restaurant.number_served))
my_restaurant.number_served = 4
print("Customers served: " + str(my_restaurant.number_served))
my_restaurant.set_number_served(10)
print("Customers served: " + str(my_restaurant.number_served))
my_restaurant.increment_number_served(3)
print("Customers served: " + str(my_restaurant.number_served))

