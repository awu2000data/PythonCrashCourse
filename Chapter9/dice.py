"""
Exercise 9-14
Use the module random, function randint()

Make a class, Die with one attribute, sides
which has a default value of 6. 

Write a method called roll_die() that prints
a random number in range of the sides on the die

Make a 6-sided die and roll it 10 times

Make a 10-sided die and roll it 10 times
"""

from random import randint

class Die():
	"""A basic representation of a dice"""

	def __init__(self, sides):
		"""Initialize the attributes of a dice"""
		self.sides = sides

	def roll_die(self):
		"""Simulate rolling a dice"""
		result = randint(1,self.sides)
		print(result)

six_sides = Die(6)
print("Rolling six sided dice")
for val in range(1,11):
	six_sides.roll_die()

print("\n")

six_sides = Die(10)
print("Rolling ten sided dice")
for val in range(1,11):
	six_sides.roll_die()