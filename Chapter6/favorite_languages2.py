favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
	}

for person, languages in favorite_languages.items():
	print(person.title() + ", your favorite languages are: ")
	for language in languages:
		print(language)
	print("\n")