"""
Exercise 7-5
A movie theatre charges
0 for ages under 3
10 for ages 3-12
15 for ages over 12
Write a loop to ask users their age
then tell them their price
"""

prompt = "\nEnter your age(-1 to quit): "
active = True
while active:
	number = int(input(prompt))
	if number == -1:
		active = False
	elif number < 3:
		print("Your ticket is free")
	elif number < 13:
		print("Your ticket is $10")
	else:
		print("Your ticket is $15")
