class calc:
    def add (self,a,b):          #Hierarchical_inheritance
        print (a+b)
class cal1(calc):
    def sub (self,a,b):
        print (a-b)
class cal2(calc):
    def mul (self,a,b):
        print(a*b)
#main
ans=cal1()
ans.add(4,3)
ans.sub(4,3)
ans1=cal2()
ans1.add(5,6)
ans1.mul(4,3)