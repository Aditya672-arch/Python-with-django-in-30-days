# list wiht member ship operator
list1=[2,56,7,9,10]
s=int(input("enter data to be search: "))
found = 0
for i in range(0, len(list1)):
    if(list1[i]==s):
        found = 1
        break
if (found == 1):
    print("data found")
else:
    print("data not found")