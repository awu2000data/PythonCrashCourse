"""
Exercise 9-8
Write a privileges class that should have
one attribute, a list, called privileges.

Move show_privileges() to this class

Make a privilege instance an attribute in
your Admin class

Make an instance of admin and show the privileges
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


class Privileges():
	"""A representation of the privileges a user holds"""

	def __init__(self):
		"""initialize the attributes of the class"""
		self.privileges = ['add post', 'delete post', 'ban user']

	def show_privileges(self):
		"""Display the privileges that the admin has"""
		print("You have the following privileges:")
		for privilege in self.privileges:
			print("- " + privilege)


class Admin(User):
	"""A representation of a specific type of user, an admin"""

	def __init__(self, first_name, last_name, age, username):
		"""
		Initialize the User class's attributes
		Then do the same for this class's attributes
		"""
		super().__init__(first_name,last_name,age,username)
		self.privileges = Privileges()		

adminA = Admin('sam', 'radford', 25, 'radfordsm2')
adminA.privileges.show_privileges()
