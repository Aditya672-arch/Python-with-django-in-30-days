def str_pal(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"

print(str_pal("MAM"))