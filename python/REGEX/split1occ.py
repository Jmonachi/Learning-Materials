import re

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)
if (x):
	print("Match detected")
else:
	print("No Match detected")