"""
Exercise 10-6
Write a program that prompts for two numbers
Add them together and print the result.
Catch TypeError if either input value is not a number.
Print a friendly error message.
"""

try:
	num1 = int(input("Enter a number: "))
	num2 = int(input("Enter a number: "))

except ValueError:
	print("You were supposed to enter a number!")
else:
	sum1 = num1 + num2
	print("Sum is: " + str(sum1))