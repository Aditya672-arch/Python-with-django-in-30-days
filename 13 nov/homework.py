#Q1 = WAP to check maximum between 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is maximum")
elif b > a:
    print(b, "is maximum")
else:
    print("Both numbers are equal")