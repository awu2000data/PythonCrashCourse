"""
Exercise 10-8
Use dogs.txt and cats.txt
Write a program that reads these files
and prints the contents of the files to the screen
Handle FileNotFound
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
	print(filename + " could not be opened")
