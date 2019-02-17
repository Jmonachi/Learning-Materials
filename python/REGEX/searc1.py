import re

txt = "The rain in Spain"
x = re.search("^The.*German", txt)
if (x):
	print("Yes, we have a match!")
else:
	print("we have no that match")


