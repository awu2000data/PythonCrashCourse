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

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test case for employee.py"""

	def setUp(self):
		"""Create a worker instance to use in all tests"""
		self.worker = Employee('Sam', 'Radford', 40000)

	def test_give_default_raise(self):
		"""Test that calling raise without passing a value works"""
		salary = self.worker.salary + 5000
		self.worker.give_raise()
		self.assertEqual(salary, self.worker.salary)
	
	def test_give_custom_raise(self):
		"""Test that calling raise with a custom value works"""
		custom_increase = 8000
		salary = self.worker.salary + custom_increase
		self.worker.give_raise(custom_increase)
		self.assertEqual(salary, self.worker.salary)	





unittest.main()