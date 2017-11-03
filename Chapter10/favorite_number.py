"""
Exercise 10-11
Write a program that prompts for the user's favorite
number.  Use json.dump() to store this number in a file.
Write a separate program that reads this value and 
prints the message, 'Your favorite number is ___'
"""
import json

number = input("What's your favorite number: ")

filename = 'fav_number.json'

with open(filename, 'w') as file_object:
	json.dump(number,file_object)
