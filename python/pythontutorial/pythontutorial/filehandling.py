a=open("handling.txt")
print(a.read(10))
print(a.readline())
a.close()

a=open("handling.txt","a")
a.write("this is added line using append.")
a.close()

a=open("handling.txt","r")
print(a.read())

import os
if os.path.exists("demofile1.txt"):
    os.remove("demofile1.txt")
else:
    print("the file doesn't exists")