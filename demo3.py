#list all operation
student = []
import sys
while True:
    print("1 for add record: ")
    print("2 for display record: ")
    print("3 for delete: ")
    print("4 remove all record: ")
    print("0 for exit: ")
    ch = int(input ("enter your choice: "))
    if (ch == 1):
        rollno = int(input("enter your roll no. "))
        name = input("enter name: ")
        marks = int(input("enter marks: "))
        x = [rollno, name, marks] 
        student.append(x)
        print("record added: ")
    elif(ch == 2):
        for x in student:
            print(x)
            print(x)
    elif(ch == 3):
            for x in student:
                print(x)
            rollno = int(input("enter roll no. to delete: "))
            for x in student:
                if x[0] == rollno:
                    student.remove(x)
                    print("record deleted: ")
    elif(ch == 4):
        for x in student:
            if x[0] == rollno:
                student.clear()
                print("record cleared: ")
        
    
    elif(ch == 0):
        sys.exit()
    else:
        print("invalid choice:")