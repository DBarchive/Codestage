class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
#main
a=int(input("enter the value of a: "))
b=int(input("enter the value of b: "))
ans=calculator()
print("addition is :", ans.add(a,b))
print("subration is :", ans.sub(a,b))
print("multiplication is :", ans.mul(a,b))
print("division :", ans.div(a,b))