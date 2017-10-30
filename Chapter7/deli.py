"""
Exercise 7-8
Make a list called sandwich_orders
and fill it with the names of
various sandwiches then make an empty list
called finished_sandwiches.  Loop through
printing a message saying you made each sandwich and
then add it to the finished_sandwiches list.
Then print each sandwich that was made
"""

sandwich_orders = ['ham', 'turkey', 'reuben', 'french dip']
finished_sandwiches = []

for sandwich in sandwich_orders:
	print("I made your " + sandwich + " sandwich")
	finished_sandwiches.append(sandwich)
print("\nFinished orders: ")
for sandwich in finished_sandwiches:
	print(sandwich)