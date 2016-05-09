# 004.py
'''
for循环
'''
print("打印1-100：")
for i in range(1, 101) :
	print(i, end='\t')
print("----------------------------------------")
print("计算1-100的和：")
sum = 0
for i in range(1, 100):
	sum += i
print("1 + 2 + 3 + ... + 100 =", sum)
print("----------------------------------------")

input("end~~~")
