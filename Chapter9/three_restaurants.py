"""
Exercise 9-2
Start with your class from 9-1
Make three instances and then
call describe_restaurant on all three
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

restaurantA = Restaurant('casalinga', 'italian')
restaurantA.describe_restaurant()
print("\n")

restaurantB = Restaurant('el dorado', 'mexican')
restaurantB.describe_restaurant()
print("\n")

restaurantC = Restaurant('jimmy johns', 'sandwich')
restaurantC.describe_restaurant()
print("\n")

