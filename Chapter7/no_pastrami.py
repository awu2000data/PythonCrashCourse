"""
Exercise 7-9
Using the list sandwich_orders from 7-8
make sure the sandwich 'pastrami' appears
at least three times. Add code near the
beginning of your program to print a message
that says that the deli has run out of pastrami.
Then use a while loop to remove all occurances
of pastrami from the list
"""

sandwich_orders = ['ham', 'pastrami', 'pastrami', 'turkey', 'reuben', 'pastrami', 'french dip']
finished_sandwiches = []

print("We have run out of pastrami")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print("\n")
print(sandwich_orders)