# WAP to check number is palindrome 
def pal(n):
    n = str(n)
    temp = n[::-1]
    if temp == n:
        return "Palindorme"
    else:
        return "Not palindorme"

print(pal(8565))