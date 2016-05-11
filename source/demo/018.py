# 018.py
class Animal(object):

	def run(self) :
		print("animal running...")

class Dog(Animal):
	
	def run(self) :
		print("dog running...")

class Cat(Animal):
	
	def run(self):
		print("cat running...")

a1 = Animal()
a2 = Dog()
a3 = Cat()
a1.run()
a2.run()
a3.run()
print("-------------------")
print(isinstance(a1, Animal))
print(isinstance(a2, Animal))
print(isinstance(a3, Animal))
print(isinstance(a1, object))
print(isinstance(a1, object))
print(isinstance(a1, object))
print("-------------------")
print(type(a1))
print(type(a2))
print(type(a3))
print("-------------------")
def threeRun(a) :
	a.run()
	a.run()
	a.run()

threeRun(a1)
threeRun(a2)
threeRun(a3)

input("end~~")
