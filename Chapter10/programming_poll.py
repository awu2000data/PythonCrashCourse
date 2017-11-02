"""
Exercise 10-5

write a while loop that asks people why they like
programming.  Each time someone enters a reason,
add that reason to a file that stores the responses
"""

filename = 'programming_responses.txt'

with open(filename, 'w') as file_object:
	while True:
		response = input("Why do you like programming?('q' to quit) ")
		if response == 'q':
			break
		file_object.write(response + '\n')
