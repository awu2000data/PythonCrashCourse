alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#A list of dictionaries
aliens = [alien_0, alien_1, alien_2]

print(aliens)
print("\n")
for alien in aliens:
	print(alien)
print("\n")

#Start with an empty list and fill with created dictionaries
aliens = []

for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("\n")
print("Num Aliens Created: " + str(len(aliens)))
print("\n")


#Modify a few aliens in the list
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'

for alien in aliens[:5]:
	print(alien)
print("\n")
