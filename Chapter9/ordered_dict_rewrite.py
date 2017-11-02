"""
Start with exercise 6.4, glossary2.py

Rewrite the program using the OrderedDict class
Make sure the order of the output is correct
"""

from collections import OrderedDict

glossary = OrderedDict()

glossary["list"] = "A sequence of items that can be accessed by index"
glossary["set"] = "A sequence with no duplicate items"
glossary["tuple"] = "A sequence that can't be modified"
glossary["dictionary"] = "A sequence of key/value pairs"
glossary["stripping"] = "Removing white space from a string"


for term, definition in glossary.items():
	print(term.title() + ": " + definition)