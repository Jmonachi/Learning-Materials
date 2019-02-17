class Mynumbers:
	
	def __iter__(self):
		self.a = 10
		return self

	def __next__(self):
		x = self.a
		self.a +=1
		return x

myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
	if x < 20:
		x +=1
		print(x)
		

		
		

#print(next(myiter))
#print(next(myiter))
##print(next(myiter))
		