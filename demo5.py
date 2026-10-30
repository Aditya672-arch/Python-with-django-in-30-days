#prg for fibonacci series
n = int(input("Enter the limit: "))
a = 0
b = 1
print(a) #0
print(b) #1
for i in range(1, n+1):
    c = a + b
    print(c)
    a = b   #a=1
    b = c   #b=1