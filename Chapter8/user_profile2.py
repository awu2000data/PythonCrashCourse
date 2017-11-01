"""
Exercise 8-13
Start with user_profile.py
Build a profile of your self using
your first and last name as well as
three other key-value pairs that describe you
"""

def build_profile(first, last, **user_info):
	"""Build a dictionary with everything we know about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('sam', 'radford',
							location='raleigh',
							field='computer science',
							age='25')
print(user_profile)