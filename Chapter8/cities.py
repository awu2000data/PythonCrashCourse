"""
Exercise 8-5
Write a function called describe_city() that
accepts the name of a city and it's country.
Print a simple sentence saying city is in country.
Give the country a default value.  Call your function
with three different cities, one not being in default.
"""

def describe_city(city, country="America"):
	print("\n" + city.title() + " is in " + country.title() + ".")

describe_city("raleigh")
describe_city("houston")
describe_city("tokyo", "japan")