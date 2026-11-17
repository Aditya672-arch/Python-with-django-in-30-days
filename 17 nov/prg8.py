import copy
a=[[1, 2, 3], [4, 5, 6]]
print(a)
b=copy.copy(a)
print(b)
b[0][0]=99
print(a)
print(b)
a[0][0]=100
print(a)
print(b)