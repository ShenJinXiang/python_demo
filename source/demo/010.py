# 010.py 列表生成式
print("range(1, 11):")
print(list(range(1, 11)))

L = []
for x in range(1, 11):
	L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([m + n for m in 'ABC' for n in 'XYZ'])
print([(m + n).lower() for m in 'ABC' for n in 'XYZ'])

d = {'name': '张三', 'age': 18, 'address': 'Beijing'}
print([k + '=' + str(v) for k, v in d.items()])

L = ['HELLO', 'WORLD', 'SHENJINXIANG']
print([i.lower() for i in L])
input("end~~~")
