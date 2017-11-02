filename = 'programming.txt'

"""
Four modes when opening a file
blank - defaults to r
1: r - read from file
2: w - write to a file
3: a - append to a file
4: r+ - read + write to a file 
"""
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")