# 011.py ceshi
def jia(x, y):
	return x + y
def jian(x, y):
	return x -y
def chen(x, y):
	return x * y
def chu(x, y):
	return x / y

def operate(x, y, fn):
	return fn(x, y)

print(operate(12, 2, jia))
print(operate(12, 2, jian))
print(operate(12, 2, chen))
print(operate(12, 2, chu))
input("end~~~")
