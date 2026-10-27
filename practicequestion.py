#Write a program to calculate area of circle - area, rectangular
# Function to calculate area of a circle
def area_of_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area  

# Function to calculate area of a rectangle
def area_of_rectangle(length, width):
    return length * width
a = 45
b= 40
print(area_of_circle(a))
print(area_of_rectangle(b, a))


#Q2= Calculate total and percentage of 5 subject  marks
marks = [20, 30, 40, 70, 95]
total = sum(marks)
percentage = (total / 500) * 100
print("Total:", total)
print("Percentage:", percentage)

#Q3= Program for swapping of two numbers with or without using third variable
x = 10
y = 20
# Swapping using a third variable
temp = x
x = y
y = temp
print("After swapping: x =", x, "y =", y)
# Swapping using without third variable
x= x + y
y = x - y
x = x - y
print("After swapping: x =", x, "y =", y)