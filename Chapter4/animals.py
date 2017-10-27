#Exercise 4-2
#Think of three animals sharing a common characteristic
#Print each animal using a for loop
#Print a statement about each animal
#Print a line saying what's common about them

animals = ['cat', 'dog', 'bunny']

for animal in animals:
	print(animal)
print("\n")

for animal in animals:
	print("A " + animal.title() + " would make a great pet")
print("These animals all share the fact that they'd be a good pet")

