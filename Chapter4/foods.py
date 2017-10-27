my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("Copying a list -> friends_foods = my_foods[:]")
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)
print("\n")

print("Append to each list to prove they are different")
my_foods.append("cannoli")
friends_foods.append("ice cream")
print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friends_foods)
print("\n")