#printing the prime numbers up to the given max range
max = int(input ("Find prime up to what number: "))

for x in range(2,max+1):
	isprime = True
	for y in range(2,x):
		if (x%y == 0):
			isprime = False
			break
	else:
		print(x)

		