# 007.py
''' 递归函数 '''
# 计算阶乘 n！ = 1 * 2 * ... * n
def fact(n=1):
	if not isinstance(n, int) :
		raise TypeError('错误的参数类型')
	if n < 1:
		print("请输入大于0的整数！")
		return
	if n == 1:
		return 1
	return fact(n - 1) * n
print(fact(1))
print(fact(2))
print(fact(9))
print(fact(100))
input("end~~~")
