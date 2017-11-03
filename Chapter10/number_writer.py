#JSON - JavaScript Object Notation

import json

numbers = [2, 3, 5, 7, 11, 13]
#json.dump takes two arguments:
#A piece of data to store
#And a file it can use to store them

filename = 'numbers.json'
with open(filename, 'w') as file_object:
	json.dump(numbers, file_object)