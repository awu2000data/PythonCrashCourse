"""
Exercise 10-2
Use the replace() method to read through your
learned_in_python.txt file and replace
every occurance of python with c
then print our the file
"""

filename = 'learned_in_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.replace('python', 'c'))

