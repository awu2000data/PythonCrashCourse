"""
Exercise 9-6
Write a class called IceCreamStand that
inherits from the Restaurant class you 
wrote in 9-1 restaurant.py.

Add an attribute called flavors that stores
a list of flavors of ice cream.

Write a method that displays these flavors.

Create an instance of the class and call display_flavors()
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

class IceCreamStand(Restaurant):
	"""A simple representation of an ice cream stand"""

	def __init__(self, name, cuisine_type, flavors):
		"""
		Initialize the parent's attributes
		Then initialize this class's attributes
		"""
		super().__init__(name, cuisine_type)
		self.flavors = flavors

	def display_flavors(self):
		"""Print a list of flavors offered"""
		print("The following flavors are offered: ")
		for flavor in self.flavors:
			print("- " + flavor.title())

flavors = ['vanilla', 'chocolate', 'strawberry', 
			'mint chocolate chip', 'mocha', 'peach',
			'rum raisen', 'peanut butter']
ice_cream = IceCreamStand('ritas', 'ice cream', flavors)
ice_cream.open_restaurant()
ice_cream.display_flavors()