#find max among 3 no. using ladder if
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(a, "is the maximum number")
elif b >= a and b >= c:
    print(b, "is the maximum number")
else:
    print(c, "is the maximum number")


