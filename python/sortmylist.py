def my_sort(a):
  
   a.sort()
   return a
def separate(mylist):
	even = []
	odd = []
	for i in mylist:
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)
	return even,odd

even,odd = 	separate([1,2,3,4,5,6,7,8,9,10])
odd = my_sort(odd)
even = my_sort(even)
odd.extend(even)

print(odd)