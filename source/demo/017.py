# 017.py
class Person(object):

	def __init__(self, name, age, address) :
		self.__name = name
		self.__age = age
		self.__address = address
	
	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name
	
	def getAge(self):
		return self.__age

	def setAge(self, age):
		self.__age = age

	def getAddress(self):
		return self.__address

	def setAddress(self, address):
		self.__address = address
	
	def printPerson(self) :
		print("%s: %s, %s: %s, %s: %s" % ('姓名', self.__name, '年龄', self.__age, '地址', self.__address))

p1 = Person('张三', 16, 'Beijing')
print(p1.getName())
print(p1.getAge())
print(p1.getAddress())
p1.printPerson()
print(dir(p1))
p1.__name='zhangsan'
print(p1.__name)
print(p1._Person__name)
input("end~~~")
