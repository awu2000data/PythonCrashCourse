def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design then move them to completed_models"""
	while unprinted_designs:
		current_deign = unprinted_designs.pop()
		print("Printing Model: " + current_deign)
		completed_models.append(current_deign)

def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print("\n")

print("Send a copy of an array so it doesn't get modified")
print("\n")

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

