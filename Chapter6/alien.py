#Create a dictionary
alien_0 = {'color': 'green', 'points': 5}

#Access values from a dictionary
print(alien_0['color'])
print(alien_0['points'])
print("\n")

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("\n")

#Adding to a dictionary
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("\n")
print(alien_0)
print("\n")

#Starting with an empty dictionary
alien_1 = {}
print(alien_1)
alien_1['color'] = "red"
alien_1['points'] = 10
print(alien_1)
print("\n\n")

#Changing values in a dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print("\n\n")

#Deleting pairs from a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)