magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print("\n")

#Everything indented is a part of the loop
#Not indenting means we're back out of the loop
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone.  That was a great magic show!")	
