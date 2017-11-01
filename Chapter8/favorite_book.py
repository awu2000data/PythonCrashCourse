"""
Exercise 8-2
Write a function called favorite_book() that accepts
one parameter, title.  The function should print a message
saying that the argument is one of your favorite books.
Call the function.
"""

def favorite_book(title):
	print("One of my favorite books is, " + title.title() + ".")

favorite_book("Norwegian Wood")