per = float(input("Enter the percentage: "))
if (per>=60):
    print("First Division")
elif(per>=45 and per<60):
    print("Second Division")
elif(per>=33 and per<45):
    print("Third Division")
else:
    print("Failed")