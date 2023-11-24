#f = open("Filehandle.txt", "r")
#print(f.read())
import os
path1 = "Filehandle.txt"

#with open(path1, "r") as a:   #always use with keyword as it automatically closes the file.
#    content = a.readline() 
#    print(content)


#using for loop to read file
#with open(path1, "r") as a:
#    for b in a:
#       print(b)

os.remove("Filehandle.txt")
if os.path.exists("Filehandle.txt"):
    os.remove("Filehandle.txt")
else:
    print("File removed")
