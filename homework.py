#Q = print sum of given series 1/1 + 1/2+...........1/n
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print("The sum of the series is:", sum)



#prg for factorial of a number
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is:", factorial)


#print sum of given series 1/1! + 1/2! + 1/3! + ...........1/n!
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum += 1 / factorial
print("The sum of the series is:", sum)


#print series 1 3 5 7 9 ..........n
n = int(input("Enter the value of n: "))
for i in range(1, n + 1, 2):
    print(i, end=" ")


#print series 2 4 6 8........n
n = int(input("Enter the value of n: "))
for i in range(2, n+1, 2):
    print(i, end=" ")
