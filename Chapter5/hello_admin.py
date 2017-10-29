#Exercise 5-8
#Make a list of usernames including 'admin'
#Loop through the list and add a greeting
#Print a special meaning for admin

user_names = ['user1', 'user2', 'admin', 'user3', 'user4']

for user in user_names:
	if user == 'admin':
		print("Hello admin, would you like to see a status report")
	else:
		print("Hello " + user + " welcome back!")
