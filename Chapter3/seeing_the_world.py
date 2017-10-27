#Exercise 3-8 
#Store five locations you want to visit in a list
#Print in the original order
#Print it sorted without changing it
#Print in the original order
#Print in reverse sorted order without changing it
#Print the original again
#Use reverse and print
#Use reverse again and print
#Use sort and print
#Use sort in reverse and print

locations = ["Japan", "Italy", "New York", "Canada", "London"]

print(locations)
print(sorted(locations))
print(locations)
print("\n")

print(locations)
print(sorted(locations, reverse=True))
print(locations)
print("\n")

print(locations)
locations.reverse()
print(locations)
print("\n")

print(locations)
locations.reverse()
print(locations)
print("\n")

print(locations)
locations.sort()
print(locations)
print("\n")

print(locations)
locations.sort(reverse=True)
print(locations)
print("\n")