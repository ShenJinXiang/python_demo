# 002.py
# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print("classmates的长度：", len(classmates))
print("classmates[0]:", classmates[0]);
print("classmates[1]:", classmates[1]);
print("classmates[2]:", classmates[2]);
print("classmates[-1]:", classmates[-1]);
print("classmates[-2]:", classmates[-2]);
print("classmates[-3]:", classmates[-3]);
print("-----------------------------")

print("末尾添加'Adam':")
classmates.append('Adam')
print(classmates)
print("-----------------------------")

print("'1'位置添加'Jack'")
classmates.insert(1, 'Jack')
print(classmates)
print("-----------------------------")

print("pop:")
print(classmates.pop())
print(classmates)
print("-----------------------------")

print("pop(1)")
print(classmates.pop(1))
print(classmates)
print("-----------------------------")

print("classmates[1] = 'Sarah':")
classmates[1] = 'Sarah'
print(classmates)
print("-----------------------------")

input("end~~~")
