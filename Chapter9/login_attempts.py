"""
Exercise 9-5
Add an attr, login_attempts to your User
class in user.py from 9-3.  

Write a method called increment_login_attempts()
that increments the value of login_attempts by 1.

Write another method, reset_login_attempts()
that sets the value of login_attempts to 0

Make an instance of the class, call increment
several times.  Print the value of login_attempts

Call reset login, then print the value again
"""

class User():
	"""A simple representation of a user profile"""

	def __init__(self, first_name, last_name, age, username):
		"""Initialze the four attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.username = username
		self.login_attempts = 0

	def describe_user(self):
		"""Print a summary of the user"""
		print("\n" + self.username + ":")
		print("Name: " + self.first_name.title() + " " + self.last_name.title())
		print("Age: " + str(self.age))

	def greet_user(self):
		"""Welcome the user back"""
		print("Welcome back, " + self.username + "!")

	def increment_login_attempts(self):
		"""Increase the login_attempts value by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Set the value of login_attempts to 0"""
		self.login_attempts = 0



userA = User('sam', 'radford', 25, 'radfordsm2')
print("Login Attempts: " + str(userA.login_attempts))
userA.increment_login_attempts()
userA.increment_login_attempts()
userA.increment_login_attempts()
print("Login Attempts: " + str(userA.login_attempts))
userA.reset_login_attempts()
print("Login Attempts: " + str(userA.login_attempts))
