a = (10, 20, 30, 40, 50)
print(a)
#a.append(60) #attreibute error
#convert tuple to list
b=list(a)
b.append(60)
#convert list to tuple
a=tuple(b)
print(a)