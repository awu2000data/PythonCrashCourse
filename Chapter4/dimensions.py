#Python calls values that cannot be changed, 'immutable'
#A list that is immutable is called a, 'tuple'
#Just like a list except with () insead of []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("\n")

print("Trying to change a value produces: ")
try:
	dimensions[0] = 400
except Exception as e:
	print(e)
print("\n")

print("Loop through a tuple")
for dimension in dimensions:
	print(dimension)
print("\n")

print("You can't modify a tuple but you can change the value the variable holds")
print("Original Dimensions: ")
for dimension in dimensions:
	print(dimension)
print("\n")
print("New Dimensions: ")
dimensions = (400,100)
for dimension in dimensions:
	print(dimension)
print("\n")