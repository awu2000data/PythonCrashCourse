"""
The other file for favorite_number.py
"""
import json

filename = 'fav_number.json'

with open(filename) as file_object:
	number = json.load(file_object)
	print("Your favorite number is: " + number)