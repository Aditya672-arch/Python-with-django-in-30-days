try:
 
 x=int(input("Enter any number: "))
 y=int(input("Enter a number: "))
 z=x/y
except ZeroDivisionError:
 print("no. must be > zero")
else:
 print("z")
finally:
 print("prg. ends here")