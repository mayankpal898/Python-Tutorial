# For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Looping Through a String
for x in "banana":
  print(x)
# break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
for x in range(6):
  print(x)
for x in range(2, 6):
  print(x)
for x in range(2, 30, 3):
  print(x)
# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
# Nested Loops
# A nested loop is a loop inside a loop.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# pass Statement
for x in [0, 1, 2]:
  pass
     


