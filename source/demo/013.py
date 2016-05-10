# 013.py 闭包
def idObj(n):
	_id = n
	return lambda: _id
o = idObj(100)
print(o)
print(o())
input("end~~~")
