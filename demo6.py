#nested list - a list within in a list 
#called nested list
a  = [[1, 2], [3, 4], [5, 6]]
print(a)
print(a[0][0])
a[0][0]=11
print(a)
print(a[2][0])
a.clear()
print(a)