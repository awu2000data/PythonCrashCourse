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

def get_formatted_location(city, country, population=''):
	if population:
		formatted = city + ", " + country + " - " + str(population)
	else:
		formatted = city + ", " + country
	return formatted.title()
