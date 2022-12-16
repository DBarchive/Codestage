import os
path="D:\Linux\shell"
with open (path,"a+") as file:
    file.writelines(input("Enter the message")+"\n")
    content=file.read()
    print(content)
    