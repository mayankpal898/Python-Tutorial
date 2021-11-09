# Global Variables
# Variables that are created outside of a function are known as global variables.
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc1():
  x = "fantastic"
  print("Python is " + x)
myfunc1()
print("Python is " + x)
# global Keyword
'''
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
'''
x = "awesome"
def myfunc2():
  global x
  x = "fantastic"
myfunc2()
print("Python is " + x)