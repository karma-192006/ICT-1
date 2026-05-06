greetings=open("hello.txt","r") #opening 
print(greetings)

greetings.close() #closing

#fileproperties
f=open("hello.txt","r")
print("filename:",f.name)
print("file mode:",f.mode)
print("Is the file closed?:",f.closed) #FALSE
f.close()
print("Is the file closed?:",f.closed) #TRUE
      
#file reading
f=open("hello.txt","r")
contents=f.read()
print(contents)
f.close()

#writing a file
newfile=open("newfile.txt","w")
print(newfile)
newfile.write("This is a new file created using Python.")
newfile.close()

#opening the file in write mode to overwrite the existing content
FileOverwrite=open("newfile.txt","w")
FileOverwrite.write("The contents of the newfile is now changed.")
FileOverwrite.close()

#append a file
appendFile=open("hello.txt","a")
appendFile.write("\n\nDon't forget to smile today!") #/n/n is used to add a new line after 2 lines
appendFile.close()

#with statement helps to automatically close the file after the block of code is executed
with open("hello.txt","r") as f:
    contents=f.read()
    print(contents)