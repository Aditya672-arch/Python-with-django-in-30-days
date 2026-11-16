#2. WAP to check given number is palindrome or not (Without passing arguments)
def palindrome():
    n = int(input("Enter a number: "))
    temp = n
    rev = 0

    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10

    if temp == rev:
        print("Palindrome number")
    else:
        print("Not a palindrome number")

palindrome()