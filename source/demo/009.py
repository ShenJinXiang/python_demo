# 009.py 迭代
print("迭代list：")
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for m in l:
	print(m, end='\t')
print()
print("----------------")

print("迭代dict:")
d = {'a': 1, 'b': 2, 'x': 'aa'}
for k in d:
	print(k, end='\t')
print()
for k in d.values():
	print(k, end='\t')
print()
for k, v in d.items():
	print(k, ':', v)
print("----------------")

s = '中华人民共和国'
for S in s:
	print(S, end='\t')
print()

input("end~~~")

