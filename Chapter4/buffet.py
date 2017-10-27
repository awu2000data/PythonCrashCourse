#Exercise 4-13
#Store five foods in a tuple
#Use a for loop to print each food
#Try to modify an item and handle it
#Rewrite the tuple due to a change in menu and print it

foods = ('rolls', 'steak', 'ham', 'oranges', 'strawberries')

for food in foods:
	print(food)
print("\n")

try:
	foods[2] = "turkey"
except Exception as e:
	print("Can't modify a tuple")
print("\n")

print("menu changed")
foods = ('rolls', 'steak', 'turkey', 'stuffing', 'strawberries')
for food in foods:
	print(food)
