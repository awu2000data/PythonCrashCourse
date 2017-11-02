"""A class to represent a simple restaurant"""

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