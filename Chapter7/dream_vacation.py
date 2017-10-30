"""
Exercise 7-10
Poll users about where they want to visit
then print through the dictionary
"""


vacations = {}

polling = True

while polling:
	name = input("\nWhat is your name? ")
	place = input("Where would you like to visit? ")
	vacations[name] = place
	again = input("Poll another person(y/n)? ")
	if again == 'n':
		polling = False
print("\n")

for person, place in vacations.items():
	print(person.title() + " wants to visit " + place.title())
