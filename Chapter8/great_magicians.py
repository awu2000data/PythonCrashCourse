"""
Take your program from 8-9
Add a function called make_great()
that adds 'the Great' to each name
"""

def make_great(names):
	names[:] = ["the Great " + name for name in names]

def show_magicians(names):
	for name in names:
		print(name.title())

names = ["Penn", "Teller", "Hudini"]
make_great(names)
show_magicians(names)
