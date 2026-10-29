#prg for print a table of a number using while loop
n = int(input("Enter a number: "))
a = 1
while (a<=10):
    result = n*a
    print(n, "*", a, "=", result)
    a+=1