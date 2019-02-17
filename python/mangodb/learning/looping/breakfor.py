fruits = ["Bananas", "Oranges", "Mangoes", "passion fruits"]
for x in fruits:
	print(x)
	if x == "Mangoes":
		break
		

# BREAKING BEFORE THE LOOP

fruits = ["Bananas", "Oranges", "Mangoes", "passion fruits"]
for x in fruits:
	if x == "Mangoes":
	     break
	print(x)


#CONTINUE USE, STOPS THE MENTION ELEMENT IN THE LIST
fruits = ["Bananas", "Oranges", "Mangoes", "passion fruits"]
for x in fruits:
	if x == "Mangoes":
	     continue
	print(x)
