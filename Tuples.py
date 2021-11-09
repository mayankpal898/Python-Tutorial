# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))
# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
# type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

