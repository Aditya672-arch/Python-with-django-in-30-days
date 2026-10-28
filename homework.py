#wap to find max among 3 numbers using multiple if
a=int(input("Enter first number:- "))
b=int(input("Enter second number:- "))
c=int(input("Enter third number:- "))
if (a>b and a>c):
    print("The maximum number is:- ",a)
if (b>a and b>c):
    print("The maximum number is:- ",b)
if (c>a and c>b):
    print("The maximum number is:- ",c)


#wap to find middle among 3 numbers using multiple if
a=int(input("Enter first number:- "))
b=int(input("Enter second number:- "))
c=int(input("Enter third number:- "))
if (a<b and a>c) or (a>c and a<b):
    print("The middle number is:- ",a)
if (b<a and b>c) or (b>c and b<a):
    print("The middle number is:- ",b)
if (c<a and c>b) or (c>b and c<a):
    print("The middle number is:- ",c)


#wap to calculate profit and loss with given cost price and selling price
cp=int(input("Enter cost price:- "))
sp=int(input("Enter selling price:- "))
if (sp>cp):
    profit=sp-cp
    print("The profit is:- ",profit)
if (cp>sp):
    loss=cp-sp
    print("The loss is:- ",loss)
if (cp==sp):
    print("There is no profit and no loss")



#wap to find max among 3 numbers using nested if
a=int(input("Enter first number:- "))
b=int(input("Enter second number:- "))
c=int(input("Enter third number:- "))
if (a>b):
    if (a>c):
        print("The maximum number is:- ",a)
    else:
        print("The maximum number is:- ",c)
else:
    if (b>c):
        print("The maximum number is:- ",b)
    else:
        print("The maximum number is:- ",c)



#wap to find max among 4 no. using multiple if
a=int(input("Enter first number:- "))
b=int(input("Enter second number:- "))
c=int(input("Enter third number:- "))
d=int(input("Enter fourth number:- "))
if (a>b and a>c and a>d):
    print("The maximum number is:- ",a)
if (b>a and b>c and b>d):
    print("The maximum number is:- ",b)
if (c>a and c>b and c>d):
    print("The maximum number is:- ",c)
if (d>a and d>b and d>c):
    print("The maximum number is:- ",d)
