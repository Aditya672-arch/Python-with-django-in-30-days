#Identity Operator
'''
Definition: Identity operators are used to compare whether two 
variables refer to the same object in memory.

Python has two identity operators:
1. is
2. is not


'''
a = [10, 20, 30]
b = a
c = [10, 20, 30]

print(a is b)
print(a is c)
print(a is not c)