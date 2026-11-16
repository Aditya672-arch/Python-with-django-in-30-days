s = "abc"
#string access manually
print(s[0])
print(s[1])
print(s[2])
#string access by loop
for i in s:
    print(i)


for i in range(0, len(s)):
    print("index- ", i, "value-", s[i])