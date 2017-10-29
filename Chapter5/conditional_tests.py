#Exercise 5-1/5-2
#Create conditional tests
#print the expected result and result

car = 'subaru'
print("Car: " + car)
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\n")
print("Is car == 'audi'? I predict False.")
print(car == 'audi')
print("\n")

drinks = ['water','milk','tea','coffee']
print("drinks: " + str(drinks))
print("Is 'water' in drinks? I predict True.")
print('water' in drinks)
print("\n")
print("Is 'sprite' in drinks? I predict False.")
print('sprite' in drinks)
print("\n")

max_age = 25
min_age = 21
print("max_age: " + str(max_age))
print("min_age: " + str(min_age))
print("Is 25 >= max_age? I predict True")
print(25 >= max_age)
print("\n")
print("Is 25 < max_age? I predict False")
print(25 < max_age)
print("\n")
print("Is 25 < max_age or 25 > min_age? I predict True")
print(25 < max_age or 25 > min_age)
print("\n")
print("Is 25 < max_age and 25 > min_age? I predict False")
print(25 < max_age and 25 > min_age)
print("\n")