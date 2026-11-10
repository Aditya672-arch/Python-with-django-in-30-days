#Apply all list methods in a tuple
a = (10, 20, 30, 40)

b = list(a)

b.append(50)
print("Append:", b)

b.insert(1, 15)
print("Insert:", b)

b.remove(30)
print("Remove:", b)

b.pop()
print("Pop:", b)

b.sort()
print("Sort:", b)

b.reverse()
print("Reverse:", b)

a = tuple(b)
print("Final Tuple:", a)