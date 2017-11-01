def greet_users(names):
	"""Print a simple greeting to each user"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

names = ['sam', 'steve', 'anne', 'greg']
greet_users(names)
