#program for dynamic list
a  = []
n= int(input("Enter the limit: "))
for i in range(0,n):
    data=int(input("enter new data: "))
    a.append (data)
print("list all data")
print(a)