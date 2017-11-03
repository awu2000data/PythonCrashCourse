"""
Exercise 11-3
- Write a class called Employee
- Take a first name, lase name, and annual salary
- Store these as attributes
- Write a method, give_raise() that adds $5000 to the salary
  by default but also accepts a different raise amount.

- Write a test case for Employee with two methods
  test_give_default_raise() and test_give_custom_raise()
- Use setup()
- Run your tests
"""

class Employee():
	"""Basic employee with name and salary"""

	def __init__(self, first, last, salary):
		"""Initialize name and salary"""
		self.first_name = first
		self.last_name = last
		self.salary = salary

	def give_raise(self, increase=5000):
		"""Give employee a raise of $5000 or a specified amount"""
		self.salary += increase


