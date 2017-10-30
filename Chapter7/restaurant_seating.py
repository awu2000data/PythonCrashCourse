"""
Exercise 7-2
Write a program that asks the user how many
people are in their dinner group.  
If the answer is more than eight then print
a message saying they will have to wait,
otherwise their table is ready.
"""

group_size = input("How many people are in your dinner party? ")
group_size = int(group_size)

if group_size > 8:
	print("You will have to wait for a table")
else:
	print("Your table is ready")