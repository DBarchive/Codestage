def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
#main
a=int(input("enter the value: "))
b=int(input("enter the value: "))
c=int(input("enter the method: "))
if c==1:
    print("Added value is: ",add(a,b))
if c==2:
    print("Subracted value is: ",sub(a,b))
if c==3:
    print("multuplication value is: ",mul(a,b))
if c==4:
    print("Divided value is: ",div(a,b))
    
    