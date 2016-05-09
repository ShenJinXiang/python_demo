# 006.py
''' 函数 '''
print("max(1, 2, 3, 3.34, 5, 0, -110, 110):", max(1, 2, 3, 3.34, 5, 0, -110, 110))

def myAbs(x):
	if x > 0:
		return x
	else:
		return -x
print("myAbs(100):", myAbs(100))
print("myAbs(0):", myAbs(0))
print("myAbs(-100):", myAbs(-100))

print("===============================")
print("默认参数")
def sayHello(name = 'world'):
	print("hello", name)
sayHello()
sayHello("ShenJinXiang")
print("-------------------------------")
print("错误的例子：")
def addEnd(L = []) :
	L.append("end")
	return L
l = [1, 2, 3]
print(addEnd(l))
print(addEnd())
print(addEnd())
print(addEnd())
print("-------------------------------")
print("修改：")
def addEnd(L = None):
	if(L is None) :
		L = []
	L.append("end")
	return L
l = [1, 2, 3]
print(addEnd(l))
print(addEnd())
print(addEnd())
print(addEnd())
print("-------------------------------")
print("可变参数")
def my_sum(*numbers) :
	sum = 0
	for n in numbers:
		sum = sum + n
	return sum
print("my_sum(1, 2):",my_sum(1, 2))
print("my_sum(1, 2, 3, 4):",my_sum(1, 2, 3, 4))
print("my_sum(*[1, 2]):",my_sum(*[1, 2]))
print("my_sum(*[1, 2, 3, 4]):",my_sum(*[1, 2, 3, 4]))
print("-------------------------------")

print("关键字参数")
def person(name, age, **kw):
	print("name:", name, "age:", age, 'other:', kw)
print("person('Micheal', 30):")
person("Micheal", 30)
print("person('Bob', 35, city='Beijing'):")
person('Bob', 35, city='Beijing')
param = {'city': 'Beijing', 'job': 'Engineer'}
person('Tom', 24, **param)

input("end~~~")
