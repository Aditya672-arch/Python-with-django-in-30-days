#to check whether a number is armstrong or not
n = int(input("Enter a number: "))
res = 0
temp = n
while(n!=0):
    a=n%10
    res=(a**3)+res
    n=n//10
if(res==temp):
    print(temp, "is an armstrong number")
else:
    print(temp, "is not an armstrong number")