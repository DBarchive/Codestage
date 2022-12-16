class cal1:
    def add(self,a,b):   #multi_level inheritance
        return a+b
class cal2(cal1):
    def sub(self,a,b):
        return a-b
class cal3(cal2):
    def mul(self,a,b):
        return a*b
#main
ans=cal3()
print(ans.add(4,1))
print(ans.sub(4,1))
print(ans.mul(4,1))