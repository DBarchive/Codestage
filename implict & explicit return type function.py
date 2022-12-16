def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def max(a,b,c):
    if a>b and a>c:
        return 'a'
    elif b>a and b>c :
        return b
    else:
        return c
#main
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=add(a,b)                #implicit
print("addition is ",d)   
print("subraction is :",sub(a,b)) #explicit
print("bigger is :",max(a,b,c))   #explicit
