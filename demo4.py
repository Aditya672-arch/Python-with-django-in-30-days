#prg for 
a = [5, 4, 1, 2, 3]
print("before sorting: ")
print(a)
n=len(a)
#for no. of rounds
for i in range(0,n):
    for j in range(0, n-1-i):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print("after sorting: ")
print(a)