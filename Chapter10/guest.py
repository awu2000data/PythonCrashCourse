"""
Exercise 10-3
Write a program that prompts the user
for their name.  Write the response into
a file named, guest.txt
"""

user_name = input("What is your name? ")


filename = 'guest.txt'
with open(filename, 'w') as file_object:
	file_object.write(user_name + "\n")