#Prg. fir students marks using console applications
students=[] #empty list

while True:
    print("1 for student record: ")
    print("2 for Display student record: ")
    print("3 for search: ")
    print("0 for exit: ")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        name=input("Enter student name: ")
        marks=[]#empty list
        for i in range(3):
            m=float(input("Enter marks: "))
            marks.append(m)
        total=sum(marks)
        per=total/3
        if(per>=60):div="I div"
        else:
            print("fail")
        #empty dictionary

        student={"name":name,
                 "marks":marks,
                 "total":total,
                 "per":per,
                 "div":div}
        #append dictionary data into list
        students.append(student)
        print("Student record added")
    elif(ch==2):
        if(len(students)==0):
            print("Record not found")
        else:
            for x in students:
                print(x["name"])
                print(x["marks"])
                print(x["per"])
    elif(ch==3):
        search=input("Enter record to search: ")
        found = False
        for s in students:
            print(s["name"])
            found=True
            break
        if(found==False):
            print("record not found")
    elif(ch==0):
        break
    else:
        print("Invalid Choice ")       
        