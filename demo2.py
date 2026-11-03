# to remove duplicate element in list
a = [10, 20, 30, 20, 30, 30, 40, 20]
print(a)
b=[]
for x in a:
    if a.count(x)>1 and x not in b:
        b.append(x)
print("element if list b: ")
print(b)