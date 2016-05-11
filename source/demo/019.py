# 019.py
class Student(object):
	
	def __init__(self, name):
		self.name = name

s = Student('Bob')
s.score = 90
print(dir(s))
input("end~~~")
