players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print("\n")

print("Slicing - print(players[0:3])")
print(players[0:3])
print("\n")

print("Slicing - print(players[:4])")
print(players[:4])
print("\n")

#Third player to the end 
print("Slicing - print(players[2:])")
print(players[2:])
print("\n")

print("Last three players - print(players[-3:])")
print(players[-3:])
print("\n")

print("Looping with slicing")
for player in players[:3]:
	print(player.title())