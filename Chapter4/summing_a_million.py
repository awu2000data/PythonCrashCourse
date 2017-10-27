#Exercise 4-5
#Make a list of the numbers 1-1million
#print the min and max
#Print the sum to see how quickly counts through a million


numbers = [value for value in range(1,1000001)]
print("Min: " + str(min(numbers)))
print("Max: " + str(max(numbers)))
print("Sum: " + str(sum(numbers)))