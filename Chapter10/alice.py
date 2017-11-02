def count_words(filename):
	"""Prints the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		#Use pass to handle the error quietly
		pass
	else:
		words = contents.split()
		num_words = len(contents)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'fakefile.txt' ,'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)