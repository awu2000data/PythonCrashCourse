print("Number Comparisons")
print("\n")

answer = 17
print("if answer != 42: print('That's not correct')")
if answer != 42:
	print("That is not correct")
print("\n")


age = 19
print("age: " + str(age))
result = str(age < 21)
print("age < 21 " + result)
result = str(age <= 21)
print("age <= 21 " + result)
result = str(age > 21)
print("age > 21 " + result)
result = str(age >= 21)
print("age >= 21 " + result)
print("\n")

print("Checking multiple conditions")
age1 = 22
age2 = 24
print("age1: " + str(age1))
print("age2: " + str(age2))
print("Check all conditions are true")
result = str(age1 >= 21 and age2 >= 21)
print("age1 >= 21 and age2 >= 21 " + result)
print("\n")
age2 = 18
print("age1: " + str(age1))
print("age2: " + str(age2))
print("Check if any conditions are true")
result = str(age1 >= 21 or age2 >= 21)
print("age1 >= 21 or age2 >= 21 " + result)
