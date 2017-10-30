current_number = 0
#Use continue to move to the next iteration of a loop
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(str(current_number))

