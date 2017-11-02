"""
Exercise 10-1
Open a blank text file and write a few lines stating
what you have learned in python so far.

Write a program that reads the file and then
prints what you've wrote three times.

Print the contents
1: By reading the entire file
2: By looping over the file object
3: By storing the lines in a list and working with it outside the open block
"""


filename = "learned_in_python.txt"

# Read the entire file
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)
	print("\n")

# Loop over the file object
with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
	print("\n")

# Store the lines in a list
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())