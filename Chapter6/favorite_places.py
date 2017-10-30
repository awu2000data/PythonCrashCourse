"""Exercise 6-9
Make a dictionary called favorite places.
Use names as keys in the dictionary.
Each name should have 1-3 favorite places as a value.
Loop through and print each name and their favorite places.
"""

favorite_places = {
	'sam': ['raleigh', 'boone', 'morehead city'],
	'anne': ['savannah', 'morehead city', 'raleigh'],
	'greg': ['charleston', 'raleigh', 'boone']
}

for person, places in favorite_places.items():
	print(person.title() + " your favorite places are: ")
	for place in places:
		print(place.title())
	print("\n")