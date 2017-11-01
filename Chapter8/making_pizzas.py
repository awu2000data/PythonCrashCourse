#import an entire module
import pizza_module

#import specific functions
from pizza_module import make_pizza

#Using 'as' to give a function an alias
from pizza_module import make_pizza as mp

#Using 'as' to give a module an alias
import pizza_module as p

#Import all functions from a module
from pizza_module import *


pizza_module.make_pizza(16, 'pepperoni')
print("\n")

make_pizza(12, 'ham')
print("\n")


mp(8, 'mushrooms', 'green peppers')
print("\n")

p.make_pizza(16, 'chicken')
print("\n")