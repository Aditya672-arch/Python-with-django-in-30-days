#write a program for find n+1  find loop odd and even number
n = int(input("Enter the number: "))
for i in range(1, n+1):
    if(i%2==0):
        print(i, end=" ")
print("It is even number")
for i in range(1, n+1):
    if(i%2!=0):
        print(i, end=" ")
print("It is odd number")