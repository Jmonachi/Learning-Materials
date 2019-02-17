numbers = []
n = int(input("Enter  the number of elements: \t"))

for i in range(1, 1+n):
	allelements = int(input("Enter elements: \t"))
	numbers.append(allelements)


even_numbers = []
odd_numbers = []


for j in numbers:
	if j%2 ==0:
		even_numbers.append(j)
	else:
		odd_numbers.append(j)

print("Even numbers list: \t", even_numbers)
print("odd_numbers list: \t", odd_numbers)