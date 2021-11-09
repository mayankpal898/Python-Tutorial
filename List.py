# List
# Lists are used to store multiple items in a single variable.
thislist = ["apple", "banana", "cherry"]
print(thislist)
# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# list() Constructor
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
 


