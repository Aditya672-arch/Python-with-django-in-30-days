#prg for unit conversion
print ("press 1 for km to meter")
print ("press 2 for meter to km")
print ("press 3 for celsius to farenheit")
print ("press 4 for farenheit to celsius")
print ("press 5 for gram to kilogram")
print ("press 6 for kilogram to gram")
ch = int(input("enter your choice:"))
value = float(input("enter value: "))
if (ch == 1):
    result = value * 1000
    print("result= ", result)
elif (ch==2):
    result = value / 1000
    print("result=", result)
elif (ch==3):
    result = (value * 9/5) + 32
    print("result=", result)
elif (ch==4):
    result = (value - 32) * 5/9
    print("result=", result)
elif (ch==5):
    result=value*1000
    print("result=", result)
elif (ch==6):
    result=value/1000
    print("result=", result)