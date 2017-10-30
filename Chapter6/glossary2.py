#Exercise 6-4
#Take your glossary file and
#Print the keys/values in a loop
#instead of individually

glossary = {
	"list": "A sequence of items that can be accessed by index",
	"set": "A sequence with no duplicate items",
	"tuple": "A sequence that can't be modified",
	"dictionary": "A sequence of key/value pairs",
	"stripping": "Removing white space from a string",	
	}

for term in glossary:
	print(term.title() + ": " + glossary[term])