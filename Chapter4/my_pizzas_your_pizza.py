#Exercise 4-11/4-12
#Start with the 4-1 exercise
#Make a copy of the list of pizza
#Call it friend_pizzas
#Add a unique new pizza to each list
#Prove each list is different
pizzas = ['cheese', 'ham', 'chicken and pepporoni']
friend_pizzas = pizzas[:]

print("My pizzas: " + str(pizzas))
print("Friends: " + str(friend_pizzas))
print("\n")

pizzas.append("meatball")
friend_pizzas.append("mushroom")
print("My favorite pizzas are: ")
for pizza in pizzas:
	print("\t" + pizza.title() + " Pizza")
print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print("\t" + pizza.title() + " Pizza")
print("\n")

