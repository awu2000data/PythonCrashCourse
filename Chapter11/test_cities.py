"""
Exercise 11-1
Write a function that accepts two paramets: city and country
The function should return a string in the form
city, country
Store the function in a module called city_functions.py
Create a file, test_cities.py that tests the function you wrote.
Write a method called test_city_country()
Run test_cities to make sure it works

Exercise 11-2
Add an optional parameter, population to the function
If there it is given, print city, country - population
Add a test called test_city_country_population
Ensure both tests pass
"""

import unittest
from city_functions import get_formatted_location

class CityCountryTestCase(unittest.TestCase):
	"""Tests for city_functions.py"""

	def test_city_country(self):
		"""Test that things like 'Santiago, Chile' work"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Test that things like 'Santiago, Chile - 5000000' work"""
		formatted_location = get_formatted_location('santiago', 'chile', 5000000)
		self.assertEqual(formatted_location, 'Santiago, Chile - 5000000')

unittest.main()