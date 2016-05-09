# 005.py
'''
字典 dict
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print("d['Michael']:", d['Michael'])
d['Adam'] = 67
print(d)
print("-------------")
print("'Adam' in d:", ('Adam' in d))
print("'Lucy' in d:", ('Lucy' in d))
print("-------------")

print("d.get('Adam'):", d.get('Adam'))
print("d.get('Lucy'):", d.get('Lucy'))

'''
set
'''
s = set([1, 2, 3])
print(s)
s = set([1, 2, 3, 4, 3, 2, 1])
print(s)
print("-------------")

print("add(5):")
s.add(5)
print(s)
print("-------------")

print("remove(5):")
s.remove(5)
print(s)
print("-------------")
input("end~~~")
