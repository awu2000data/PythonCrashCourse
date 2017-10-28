#A test that can be calculated as True or False
#is a 'conditional test' such as in the if statement


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print("\n")
print("Conditional Test - is the car a bmw")
for car in cars:
	print(car == 'bmw')