try:

     student={"rno":1, "name":"xyz"}
     print(student["city"])
except KeyError:
 print("Key not found")