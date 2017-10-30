pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print("\nRemoving all Cats\n")
while 'cat' in pets:
	pets.remove('cat')
print(pets)