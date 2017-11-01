"""
Exercise 8-6
Write a function, city_country() that
takes the name of a city and a country
and returns a string formatted as:
"city, country"
Call your function three times and print the result
"""

def city_country(city, country):
	"""Takes a city and country and formats them as city, country"""
	formatted = city + ", " + country
	return formatted.title()

location = city_country("raleigh", "USA")
print(location)
location = city_country("toronto", "canada")
print(location)
location = city_country("tokyo", "japan")
print(location)