# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
# Access the Elements of an Array
print(x)
# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)
# Length of an Array
print(len(cars))
# Looping Array Elements
for x in cars:
  print(x)
# Adding Array Elements
cars.append("Honda")
print(cars)
# Removing Array Elements
cars.pop(1)
print(cars)
