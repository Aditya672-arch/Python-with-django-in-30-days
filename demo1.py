#to remove duplicate in list
a = [10, 20, 30, 40, 50, 50, 50 ,40, 30, 20]
print(a)
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)