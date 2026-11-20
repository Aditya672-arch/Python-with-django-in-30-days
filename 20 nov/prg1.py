x=open("students.txt","w")
a=["roll no - 1 name - ram",
   "roll no - 2 name - xyz",
   "roll no - 3 name - zbc" ]
x.writelines(a)
print("file created ")
x.close()