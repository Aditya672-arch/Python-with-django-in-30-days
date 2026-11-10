#Find maximum and minimum in a tuple without built-in functions
a = (10, 50, 20, 5, 40)

maximum = a[0]
minimum = a[0]

for i in a:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)