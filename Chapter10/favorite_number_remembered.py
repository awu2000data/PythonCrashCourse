"""
Exercise 10-12
Combine the two programs from 10-11 into one file
If the number is already stored, print it
Otherwise prompt for it and store it in a file.
Run it twice to ensure it works
"""
import json

filename = 'fav_number_remembered.json'

try:
	with open(filename) as file_object:
		number = json.load(file_object)
		print("Your favorite number is: " + number)

except FileNotFoundError:
	number = input("What's your favorite number: ")
	with open(filename, 'w') as file_object:
		json.dump(number,file_object)








