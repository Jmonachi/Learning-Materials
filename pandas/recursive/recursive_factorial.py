def recursive_factorial(n):
	if n < 0:
		return "Please enter a number from zero and above"
	elif n < 2:
		return 1
	else:
		return n * recursive_factorial(n-1)

#Iterative factorial
def iterative_factorial(n):
	if n < 0:
		return "Please enter a number from zero and above"
	elif n < 2:
		return 1
	else:
		fact = 1
		for a in range(1, n + 1):
			fact *= a
		return fact


print(recursive_factorial(-1))
print(iterative_factorial(5))