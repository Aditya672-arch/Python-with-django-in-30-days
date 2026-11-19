#nested list
a=[[1, 2],[1, 2], [3, 4]]
print(a)
b=[] #empty list
for x in a:
    if x not in b:
        b.append(x)
print("data in list b ")
print(b)