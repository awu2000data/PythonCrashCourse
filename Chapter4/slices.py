#Exercise 4-10
#Use slices to do the following
#Print the first three items
#Print the middle three items
#Print the last three items

numbers = [value for value in range(1,21)]

print("The first three numbers are ")
print(numbers[:3])
print("\nThree items from the middle are ")
print(numbers[8:11])
print("\nThe last three numbers are ")
print(numbers[-3:])