import os
if(os.path.exists("students.txt")):
    fp=open("students.txt", "r")
    s=fp.read()
    print(s)
else:
    print("file not found")
        