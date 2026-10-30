
# Pattern 1
for i in range(1, 4):
    for j in range(97, 97 + i):
        print(chr(j), end="")
    print()

print()

# Pattern 2
for i in range(1, 4):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

print()

#project 3

num = 1
for i in range(1, 4):
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num + 1
    print()

print()


#project 4
for i in range(1, 4):
    for j in range(1, i + 1):
        print(2 * j - 1, end=" ")
    print()
