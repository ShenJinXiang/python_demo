# 012.py map reduce filter sorted
from functools import reduce
def fn(x) :
	return x * x
def fn1(x) :
	return -x
print(list(map(fn, range(1, 21))))
print(list(map(fn1, range(1, 21))))
print("-----------------------")
def fn2(x, y) :
	return x + y
def fn3(x, y) :
	return 10 * x + y
print(reduce(fn2, list(range(1, 21))))
print(reduce(fn3, list(range(1, 21))))
print("-----------------------")
def fn4(x) :
	return x % 2 == 0
print(list(filter(fn4, range(1, 21))))
print("-----------------------")
L = [36, 5, -12, 9, -21]
print(sorted(L))
print(L)
input("end~~~")
