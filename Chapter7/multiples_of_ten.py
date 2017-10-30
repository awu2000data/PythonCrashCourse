"""
Exercise 7-3
Ask the user for a number and then report
whether or not the number is a multiple of ten
"""

number = input("Enter a number and I will tell you if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is a multiple of 10")
else:
	print(str(number) + " is not a multiple of 10")