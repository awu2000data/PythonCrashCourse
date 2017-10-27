#Exercise 4-8/4-9
#A cube is a number to the third power
#Create a list of the cubes of 1-10
#Use a for loop to print the list

cubes = [value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)