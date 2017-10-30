favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

#Retrieve one value from the dictionary by key
print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title())
print("\n")

#Loop through the dictionary and get each key
for key in favorite_languages.keys():
	print(key.title() + " thank you for taking the poll")
print("\n")

#Loop through the keys and get its value
for name in favorite_languages.keys():
	print(name.title() + " I see your favorite language is "
	 + favorite_languages[name])
print("\n")

#Check if a key isn't in the dictionary
check_name = 'erin'
if check_name not in favorite_languages.keys():
	print(check_name + ", you haven't taken the poll")
print("\n")

#Get the keys in a specific order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")
print("\n")

#Get the values from the dictionary
print("The following languages were chosen: ")
for language in favorite_languages.values():
	print(language)
print("\n")


#Get the values minus duplicates by using a set
print("The following languages were chosen: ")
for language in set(favorite_languages.values()):
	print(language)
print("\n")