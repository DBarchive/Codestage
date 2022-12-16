class cal1:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add (self):
        return self.x+self.y
    def mul(self):
        return self.x * self.y
class cal2(cal1):
    def sub(self,a,b):
        return a-b
#main
ans=cal2(4,3)
print(ans.add())
print(ans.mul())
print(ans.sub(5,4))