"""
Exercise 8-9
Create a list of names.
Pass the list to a function called show_magicians()
It prints the name of each magician
"""

def show_magicians(names):
	for name in names:
		print(name.title())

names = ["Penn", "Teller", "Hudini"]
show_magicians(names)
