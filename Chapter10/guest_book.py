"""
Exercise 10-4
Write a for loop that prompts users for their name.
When they enter, print a message to the screen tp
greet them.  After greeting them, record their name
in a file called guest_book.txt.  Make sure each entry
appears on a new line.
"""

filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
	while True:
		user_name = input("What is your name('q' to quit')? ")
		if user_name == 'q':
			break
		print("Welcome, " + user_name.title() + "!")
		file_object.write(user_name + "\n")
