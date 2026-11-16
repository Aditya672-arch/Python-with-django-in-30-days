#5. WAP to check whether a passed string is palindrome or not
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome string")
    else:
        print("Not a palindrome string")

a = input("Enter a string: ")
palindrome(a)