import re

str = "The rain in Spain"
x = re.split("\s", str)
print(x)
if (x):
	print("The match  has been detected")
else:
	print("No match detected")