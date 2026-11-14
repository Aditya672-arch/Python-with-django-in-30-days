def swap():
    a = int(input("Enter first number: "))
    b = int(input("Enter second numeber: "))
    print("before swap a=", a,"b= ", b)
    c=a
    a=b
    b=c
    print("after swap a=", a,"b= ",b)
#function calling
swap()