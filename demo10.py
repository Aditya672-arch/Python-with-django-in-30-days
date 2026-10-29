#program for palindrome number
n = int(input("Enter any number: "))
res = 0
temp = n
print("before reverse", temp)
while(n!=0):
    a = n%10
    res = (res*10)+a
    n=n//10
if(res==temp):
    print(temp, "is a palindrome number")
else:
    print(temp, "is not a palindrome number")