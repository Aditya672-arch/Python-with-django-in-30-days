#prg for string reverse
s= input("Enter your string: ")
print("Before reverse - ", s)
rev = ""
for i in s:
    rev=i+rev
print("after reverse - ", rev)