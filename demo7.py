#program for prime number
n=int(input("Enter the number: "))
found=0
for i in range(2,n):
    if(n%i==0):
        found=1
        break
if(found==1):
    print(n,"is not prime number")
else:
    print(n,"is prime number")