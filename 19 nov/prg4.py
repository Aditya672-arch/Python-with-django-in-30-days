#create a new file
fp=open("myfile.txt","w")
print(type(fp))
print("mode- ", fp.mode)
print("file name- ", fp.name)
print("file status- ", fp.closed)
data=input("Enter data in a file: ")
fp.write(data)
print("File created")
fp.close() #to close a file
print("file status -", fp.closed)