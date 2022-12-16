class parent1:
    def add (self,a,b):          #hybrid inheritance
        return a+b
class child1(parent1):
    def sub(self,a,b):
        return a-b
class parent2:
    def mul(self,a,b):
        return a*b
class child2 (child1,parent2):
    def div (self,a,b):
        return a/b
#main
ans=child2()
print (ans.add(4,3))
print (ans.sub(4,3))
print (ans.mul(4,3))
print (int(ans.div(4,2)))