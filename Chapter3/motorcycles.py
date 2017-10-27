#Adding/Modifying elements of a list

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
print("set motorcycles[0] to ducati")
motorcycles[0] = "ducati"
print(motorcycles)
print("\n")

motorcycles[0] = "honda"
print("append ducati to the original list")
motorcycles.append("ducati")
print(motorcycles)
print("\n")

print("start with an empty list and then append each item")
motorcycles = []
print(motorcycles)
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
print("\n")

print("insert an element into a list using insert")
motorcycles.insert(0, "ducati")
print(motorcycles)
print("\n")

print("remove an item from a list using del")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print("\n")

print("Use pop to remove the last item and be able to use it")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("popped: " + popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
motorcycles.append("suzuki")
print("\n")

print("You can pop from any index")
first_motorcycle = motorcycles.pop(0)
print("The first motorcycle I owned was a: " + first_motorcycle.title() + ".")
print("\n")

print("removing an item by value")
motorcycles = ["honda", "yamaha", "suzuki","ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print("motorcycles.remove('ducati'): " + str(motorcycles))
print("\n")

print("using an item removed by value")
motorcycles = ["honda", "yamaha", "suzuki","ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive + " is too expensive for me.")
print("\n")