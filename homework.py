# wap to find diff - diff area using menu driven program
print("----- AREA CALCULATOR -----")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Square")
print("4. Area of Triangle")

ch = int(input("Enter your choice: "))

if ch == 1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif ch == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area of Rectangle =", area)

elif ch == 3:
    s = float(input("Enter side: "))
    area = s * s
    print("Area of Square =", area)

elif ch == 4:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of Triangle =", area)

else:
    print("Invalid Choice")


#find even/odd no. in list
a = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)



#Find first maximum and second maximum in a list
a = [10, 50, 30, 80, 60]

a.sort()

print("First Maximum:", a[-1])
print("Second Maximum:", a[-2])


#Find duplicate elements in a list
a = [10, 20, 30, 20, 40, 10, 50]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            print("Duplicate element:", a[i])
            break

#Find sum and product of list elements
a = [2, 3, 4, 5]

sum = 0
product = 1

for i in a:
    sum = sum + i
    product = product * i

print("Sum of elements:", sum)
print("Product of elements:", product)