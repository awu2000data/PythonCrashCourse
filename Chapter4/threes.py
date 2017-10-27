#Exercise 4-7
#Make a list of multiples of 3 from 3-30 inclusive
#Use a for loop to print the numbers

threes = [value for value in range(3,31,3)]
for number in threes:
	print(number)