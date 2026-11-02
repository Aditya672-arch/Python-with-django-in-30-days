list1=[2,56,45,67,89]
print(list1)    
max1=list1[0]
for i in range(0,len(list1)):
    if(list1[i]>max1):
        max1=list1[i]
print("max number is -",max1)