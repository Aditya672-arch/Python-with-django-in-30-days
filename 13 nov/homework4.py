#4. WAP to check if a string is all lowercase or not using function
def lowercase(s):
    if s.islower():
        print("String is in lowercase")
    else:
        print("String is not in lowercase")

a = input("Enter a string: ")
lowercase(a)