#dynamic set
s=set() #empty set
print(type(s))
n= int(input("enter the limit: "))
for i in range(0, n):
    data = int(input("Enter new data: "))
    s.add(data)
print(s)