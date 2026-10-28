a = 54
print(id(a))
b = 45
print(id(b))
res=a is not b
print(res)

a = 54
print(id(a))
b = 45
print(id(b))
res=a is b
print(res)