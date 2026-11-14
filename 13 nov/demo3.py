#Pattern Program
n= int(input("Enter the limit: "))
for i in range(n, 1, -1):
    if(i%2==0):
        #increasing order
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    else:
        #decreasing order
        for j in range(i-1, 0, -1):
            print(j,end=" ")
        print()