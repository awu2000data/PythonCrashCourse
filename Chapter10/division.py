print("Give me two numbers and I'll divide them.")

first_number = int(input("\nFirst Number: "))
second_number = int(input("Second Number: "))

try:
	result = first_number / second_number
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print(str(result))