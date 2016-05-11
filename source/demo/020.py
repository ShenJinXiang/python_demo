#020.py
class Student(object):

	def __init__(self, name):
		self.name = name

print(Student('Bob'))
print("--------------")
class Person(object):

	def __init__(self, name):
		self.name = name
	
	def __str__(self) :
		return "Person : " + self.name

print(Person('Bob'))
input("end~~~")
