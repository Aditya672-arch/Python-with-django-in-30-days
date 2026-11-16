#Memborship operator
s1="python is a programming language"
print(s1)
search=input("enter data to be search: ")
result=search in s1
if(result):
    print("string found")
else:
    print("String not found")
