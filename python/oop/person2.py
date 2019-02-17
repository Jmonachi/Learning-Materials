class Robot:
	#Defining a constructor
	def __init__(self, name,color, weight):
		self.name = name
		self.color = color
		self.weight = weight

	
	def introduce_self(self):
		print("my name is " + self.name + " my favourite color is " + self.color + " and my weight in kg is ", self.weight )

r1 = Robot("James","red", 80)
r2 = Robot("Monachi","blue",70)	

#Manualy  
#r1 = Robot()
#r1.name = "James"
#r1.color = "red'"
#r1.weight = "80kg"

#r2 = Robot()
#r2.name = "Monachi"
#r2.color = "blue'"
#r2.weight = "70kg"

#r1.introduce_self()
#r2.introduce_self()


class Person:
	"""docstring fo Person"""
	def __init__(self, n,p,i):
				self.name = n
				self.personality = p
				self.is_is_sitting = i

	def sit_down(self):
		self.is_is_sitting = True


	def stand_up(self):
		self.is_is_sitting = False


p1 = Person("Alice", "Aggressive", True)
p2 = Person("Betty", "Talkative", False)



p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self()
		