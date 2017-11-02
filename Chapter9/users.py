"""
Exercise 9-3
Make a class called User.
Create two attr: first_name and last_name
Create several other attr common to users
Create a method called describe_user
Create a method called greet_user
Create a couple of instances and call both methods
"""

class User():
	"""A simple representation of a user profile"""

	def __init__(self, first_name, last_name, age, username):
		"""Initialze the four attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.username = username

	def describe_user(self):
		"""Print a summary of the user"""
		print("\n" + self.username + ":")
		print("Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))

	def greet_user(self):
		"""Welcome the user back"""
		print("Welcome back, " + self.username + "!")


userA = User('sam', 'radford', 25, 'radfordsm2')
userB = User('steve', 'radford', 28, 'sgrad')
userC = User('greg', 'radford', 60, 'gassrad')

userA.describe_user()
userA.greet_user()

userB.describe_user()
userB.greet_user()

userC.describe_user()
userC.greet_user()
