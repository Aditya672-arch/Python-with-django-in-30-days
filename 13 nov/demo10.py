#wap to find middle aming 3 no.s using function.
a = int(input("Enter first number: "))
b= int (input("Enter second number: "))
c = int(input("Enter third number: "))
if (a>b and a<c) or (a>b and a<c):
        print("middle number is: ",a)

if (b>a and b<c) or (b>c and b<a):
        print("middle number is: ",b)
else:
        print("middle number is: ",c)