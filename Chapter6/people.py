#Exercise 6-7
#take your person.py and add two new dictionaries
#add all three to a list called people
#loop through the list and print everything you know about them

eric = {
	'first_name': 'eric',
	'last_name': 'barnes',
	'city': 'Raleigh',
	}
sam = {
	'first_name': 'sam',
	'last_name': 'radford',
	'city': 'Raleigh',
	}
anne = {
	'first_name': 'anne',
	'last_name': 'radford',
	'city': 'Raleigh',
	}

people = [eric, sam, anne]

for person in people:
	name = person['first_name'] + " " + person['last_name']
	location = person['city']
	print("Name: " + name.title() + ". Location: " + location.title() + ".")