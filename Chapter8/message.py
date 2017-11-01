"""
Exercise 8-1
Write a function called display_message()
that prints a sentence telling everyone
what you are learning about in the chapter.
Then call the function.
"""

def display_message():
	message = "In this chapter we are learning about functions. "
	message += "\nWe are learning how to define them, call them, and pass them arguments. "
	message += "\nWe will also learn how to store functions in separate files called 'modules'."
	print(message)

display_message()
