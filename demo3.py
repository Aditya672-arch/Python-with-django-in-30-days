#program for different different airthmetic operations
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
ch=int(input("Enter your choice: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if ch==1:
    c=a+b
    print("sum=", c)
if ch==2:
    c=a-b
    print("sub=", c)
if ch==3:
    c=a*b
    print("mul=", c)
if ch==4:
    c=a/b
    print("div=", c)
