#swapping code
#with passing arguements 
def swap(a, b):
    temp = a
    a = b
    b = temp

    print("After swapping:")
    print("a =", a)
    print("b =", b)

# Passing arguments
x = 10
y = 20

swap(x, y)