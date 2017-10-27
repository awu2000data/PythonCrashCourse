cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print("cars.sort()")
print(cars)
print("\n")

cars.sort(reverse=True)
print("cars.sort(reverse=True)")
print(cars)
print("\n")

print("Here is the original list ")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print("\n")
print("Here is the sorted list - sorted(cars): ")
print(sorted(cars))
print("\n")
print("Here is the original list again: ")
print(cars)
print("\n")

print("Reverse the list using cars.reverse()")
print(cars)
cars.reverse()
print(cars)
print("\n")

print("Identify the length of a list")
length = len(cars)
print("There are " + str(length) + " cars in the list")