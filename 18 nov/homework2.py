#2. Check String Palindrome Using Function
def palindrome():
    s = input("Enter a string: ")

    if s == s[::-1]:
        print("Palindrome String")
    else:
        print("Not Palindrome String")


palindrome()