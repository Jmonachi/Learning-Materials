class person:
	
	def __init__(self, age, name):
		self.age = age
		self.name = name

	def myfunction(self):
		print("Hello my name is  " + self.name + " and am", self.age)


p1 = person(30, "John")
p1.myfunction()
		