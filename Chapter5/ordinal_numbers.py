#Exercise 5-11
#Ordinal numbers indicate their position in a list
#Such as 1st 2nd 3rd 4th
#Store the numbers 1-9
#loop through and print the ordinal ending for each

numbers = [value for value in range(1,10)]

for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(str(number) + "th")