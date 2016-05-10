# 014.py 
def now():
	print('2016-05-12')
f = now
f()

def log(func) :
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def printNow():
	print("pring now date~~~")

printNow()
print("end~~~")
