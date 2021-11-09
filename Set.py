# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, and unindexed.
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered
# Unordered means that the items in a set do not have a defined order.
# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(set1))
print(type(set2))
print(type(set3))
set1 = {"abc", 34, True, 40, "male"}
print(set1)
# set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
