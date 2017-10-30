name = input("Please enter your name: ")
print("Hello, " + name + "!")
print("\n")

#Build a prompt if it will take more than one line
#Then pass the prompt variable to input

prompt = "If you tell us who you are, we can personalize what you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print("Hello, " + name + "!")
print("\n")

age = input("How old are you? ")
try:
	age > 20
except Exception as e:
	print("Input comes in as a string")
	print("Trying to use it as an int produces: ")
	print(e)
print("\n")

age = input("How old are you? ")
print(age)
age = int(age)
if age >= 18:
	print("You are old enough to vote")
else:
	print("You are not old enough to vote")
