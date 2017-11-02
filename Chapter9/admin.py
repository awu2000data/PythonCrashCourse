"""
Exercise 9-7
Write a class call Admin that inherits from User
from 9-3, users.py.
Add attr, privileges that stores a list of strings
like 'can add post', 'can deslete post', 'can ban user'
Write a method called show_privileges() that lists
the admin's set of privileges.
Create an instance and call this method
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


class Admin(User):
	"""A representation of a specific type of user, an admin"""

	def __init__(self, first_name, last_name, age, username):
		"""
		Initialize the User class's attributes
		Then do the same for this class's attributes
		"""
		super().__init__(first_name,last_name,age,username)
		self.privileges = ['add post', 'delete post', 'ban user']

	def show_privileges(self):
		"""Display the privileges that the admin has"""
		print(self.username + " has the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)


adminA = Admin('sam', 'radford', 25, 'radfordsm2')
adminA.show_privileges()
