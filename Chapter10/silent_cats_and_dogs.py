"""
Exercise 10-9
Modify cats_and_dogs.py to fail silently
"""

try:
	filename = 'dogs.txt'
	with open(filename) as file_object:
		for line in file_object:
			print(line.strip())

	print("\n")

	filename = 'cats.txt'
	with open(filename) as file_object:
		for line in file_object:
			print(line.strip())		

	print("\n")

	filename = 'notafile.txt'
	with open(filename) as file_object:
		for line in file_object:
			print(line.strip())	

except FileNotFoundError:
	pass
