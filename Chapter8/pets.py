#1: Positional arguments 
#2: Keyword arguments
#3: Default values

def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#Positional Arguements:  Arguments passed in the same order
#As they are listed as parameters in the function definition.
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
print("\n")

#Keyword Arguments: A key-value pair you pass to a function
#This associates the name and value within the argument
#This keeps you from having to correctly order your arguments
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
print("\n")


#Default arguments must follow non-default
def describe_pet2(pet_name, animal_type="dog"):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet2(pet_name='willie')
describe_pet2('emmy', 'cat')
print("\n")


#Argument errors
try:
	describe_pet()
except Exception as e:
	print("Calling describe_pet() without arguments gives the error: ")
	print(e)