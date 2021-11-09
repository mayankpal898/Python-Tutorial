# Now we can use the module we just created, by using the import statement:
import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)
# Built-in Modules
import platform
x = platform.system()
print(x)
# Using the dir() Function
import platform

x = dir(platform)
print(x)