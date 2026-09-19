# sets!!

numbers = {1, 2, 3, 4, 5, 6}
# sets cant have dupes
set() # this is to define an empty set, only this way

numbers.add(7)
# adds an element 

numbers.remove(7) # raises KeyError if element not found
numbers.discard(7) # doesnt do that
# both removes elements from sets

alsonumbers = {2, 3, 4}

alsonumbers.issubset(numbers) # True
# issubset(set) checks if the set has all the elements of a set
numbers.issuperset(alsonumbers) # True
# vice-versa
numbers.isdisjoint(alsonumbers) # False
# Checks if a set doesnt have any common elements

numbers | alsonumbers # returns a new set with mixed elements
numbers & alsonumbers # returns a new set with only common elements
numbers - alsonumbers # returns a new set with the elements in the first set that arent in the other
numbers ^ alsonumbers # returns a new set with uncommon elements from both
# if you add an equal sign (|=, &=, -=, ^=), this assigns the returned set to the first set

# modules

import math# module name
# math is for math, random is for random numbers, re is for expressions, datetime is for time

# module.module_function()
math.sqrt(36) # square root of 36

import math as m
m.sqrt(36)
# putting 'as' is a way to shorten them

# from module_name import name1 as alias1, name2 as alias2
# this is for importing singular elements from a module
from math import radians, sin, cos
sine = sin(40)
# importing singular makes it so that you can call module functions directly
from math import *
# the same as above, but imports everything
# kind of discouraged, leads to namespace collision