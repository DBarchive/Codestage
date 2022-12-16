class parent:
    def add(self,a,b):
        return a+b
class child(parent):
    def sub (self,a,b):
        return a-b
class grandchild(child):  #combination of hirarichical and multilevel inheritance
    def mul(self,a,b):
        return a*b
class parent2:
    def string1(self):
        return "parent"
class child2(parent2):
    def string2(self):
        return "child"
class child3(parent2):
    def string3(self):
        return "child3"
class child4(child3,grandchild,child2):
    def div (self,a,b):
        return a/b
#main
ans=child4()
print(ans.add(4,3))
print(ans.sub(4,3))
print(ans.mul(4,3))
print(ans.string1())
print(ans.string2())
print(ans.string3())
