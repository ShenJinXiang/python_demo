# 016.py
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}
def print_score(std):
	print('%s: %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)
print("------------------")
class Student(object):
	
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def print_score(self):
		print('%s : %s' % (self.name, self.score))
	
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 80:
			return 'B'
		elif self.score >= 70:
			return 'C'
		elif self.score >= 60:
			return 'D'
		else:
			return 'E'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpsom', 87)
bart.print_score()
lisa.print_score()
print(bart.name)

print(bart.get_grade())
print(lisa.get_grade())
input("end~~~")
