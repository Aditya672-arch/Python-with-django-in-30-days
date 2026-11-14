#Prg for grade calculator
name = input("Enter your name:")
p = float(input("enter physics marks"))
c = float(input("enter chemistry marks"))
m = float(input("enter maths marks"))
total= p+c+m
per=total/3
if(per>=90 and per<=100):
    grade="A+"
elif(per>=80 and per<90):
    grade="A" 
elif(per>=70 and per<80):
    grade="B" 
elif(per>=60 and per<70):
    grade="C"
else:
    grade="E"
print("Student name: ",name)
print("Physics: ",p)
print("Chemistry: ",c)
print("Maths: ",m)
print("Total marks: ",total)
print("Percentage: ",per)
print("Grade: ",grade)