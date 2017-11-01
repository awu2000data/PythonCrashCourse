"""
Exercise 8-15
Put the functions from print_models.py
in a file called printing_functions.py.
Import those functions and use them.
"""

from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['android case', 'robot', 'sphere']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
