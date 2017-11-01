"""
Exercise 8-4
Modify the make_shirt function so that
shirts are large by default.  The message should 
default to I love Python.
The function should summarize the size and message.
1: Make a large shirt with def message
2: Make a medium shirt with def message
3: Make a shirt of any size with a different message
"""

def make_shirt(size="l", message="I love Python"):
	print("\nThe " + size.upper() +
		" shirt will be printed with the following message: ")
	print(message)

make_shirt()
make_shirt(size="m")
make_shirt("xl", "I love Java")
