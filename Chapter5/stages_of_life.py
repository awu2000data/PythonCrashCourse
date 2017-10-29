#Exercise 5-6
#Write an ifelifelse chain that
#determines a person's stage of life

age = 25
print("Age: " + str(age))

if age < 2:
	print("You are a baby")
elif age < 4:
	print("You are a toddler")
elif age < 13:
	print("You are a kid")
elif age < 20:
	print("You are a teenager")
elif age < 65:
	print("You are an adult")
else:
	print("You are an elder")