"""Exercise 7-1
Write a program that asks the user what kind
of rental car they would like.  Print a message
about that car, such as 
'let me see if I can find a ___'
"""

car = input("What type of rental car would you like? ")
print("Let me see if I can find a " + car.title() + ".")