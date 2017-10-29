#Exercise 5-9
#Take exercise 5-8
#Add an if statement to make sure the list isn't empty
#If it is say we need more users

user_names = []

if user_names:
	for user in user_names:
		if user == 'admin':
			print("Hello admin, would you like to see a status report")
		else:
			print("Hello " + user + " welcome back!")
else:
	print("We need some users!")