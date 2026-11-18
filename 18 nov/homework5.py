#5. Generate Fibonacci Series Using Function
def fibonacci():
    n = int(input("Enter number of terms: "))

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c


fibonacci()