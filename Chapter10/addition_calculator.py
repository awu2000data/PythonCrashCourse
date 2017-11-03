"""
Exercise 10-7
Wrap your 10-6, addition.py in a while loop.
"""

again = 'y'
while again == 'y':
	print("\n")
	try:
		num1 = int(input("Enter a number: "))
		num2 = int(input("Enter a number: "))
	
	except ValueError:
		print("You were supposed to enter a number!")

	else:
		sum1 = num1 + num2
		print("Sum is: " + str(sum1))

	again = input("Again? (y/n): ")