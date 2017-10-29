#Exercise 5-10
#create a list of current users and new users
#loop through new users and if the name is
#taken print they need a new username
#otherwise print a message saying it is available

current_users = ['user1', 'user2', 'admin', 'user3', 'user4']
new_users = ['User1', 'user44', 'user20', 'uSer3', 'user22']

for user in current_users:
	user.lower()

for user in new_users:
	if user.lower() in current_users:
		print(user + " is taken")
	else:
		print(user + " is available") 
