# 021.py 多重继承
class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Bat(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass


input("end~~~")
