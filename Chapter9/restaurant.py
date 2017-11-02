"""
Exercise 9-1
Make a class called Restaurant. 
Store two attributes, name and cuisine type.
Make a method called describe_restaurant that
prints these two pieces of information.
Make a method called open_restaurant that
prints a message indicating that the restaurant is open.
Make an instance of the class, print both attributes,
and call both methods.
"""


class Restaurant():
	"""A simple representation of a restaurant"""

	def __init__(self, name, cuisine_type):
		"""Initialize name and cuisine_type"""
		self.name = name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Print the name and what it serves"""
		print(self.name.title() + " serves " + self.cuisine_type + " food.")

	def open_restaurant(self):
		"""Alert that the restaurant is open"""
		print(self.name.title() + " is now open!")

my_restaurant = Restaurant('casalinga', 'italian')
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


