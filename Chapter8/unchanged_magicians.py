"""
Take your program from 8-10
Call make_great with a copy of magicians
Return the new list and store it in a separate list
Call show_magicians on each list
"""

def make_great(names):
	changed = ["the Great " + name for name in names]
	return changed

def show_magicians(names):
	for name in names:
		print(name.title())

unchanged = ["Penn", "Teller", "Hudini"]
great = make_great(unchanged[:])
show_magicians(unchanged)
show_magicians(great)
