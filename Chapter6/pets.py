"""Exercise 6-8
Make several dictionaries where the name
is the name of a pet.
In each dictionary include the kind of animal
and the owner's name.
Store the dictionaries in a list called pets
Loop through the list and print everything you know
"""

wigglesworth = {
	'name': 'wigglesworth',
	'kind': 'cat',
	'owner': 'sam',
}

emmy = {
	'name': 'emmy',
	'kind': 'cat',
	'owner': 'sam',
}

marble = {
	'name': 'marble',
	'kind': 'cat',
	'owner': 'anne',
}

momo = {
	'name': 'momo',
	'kind': 'dog',
	'owner': 'courtney',
}

pets = [wigglesworth, emmy, marble, momo]

for pet in pets:
	print(pet['name'].title() + " is a " + pet['kind'] +
		" owned by " + pet['owner'].title())
