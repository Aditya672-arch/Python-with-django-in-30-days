try:
    fp =open("students.txt","r")
    s=fp.read()
except FileNotFoundError:
    print("file not found")
else:
    print("file content:- ",s)