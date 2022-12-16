class clas1:
    def fact(self,n):
        fac=1
        for i in range (1,n+1):               #multiple_inheritance
            fac=fac*i
        return fac
        
class clas2:
    def pat(self):
        for i in range (1,4):
            for j in range (1,i+1):
                print("*",end=' ')
            print()
        print()
class clas3(clas1,clas2):
    def rev(self):
        for i in range (1,4):
            for j in range(i,4):
                print("*",  end =' ')
            print()
#main
ans=clas3()
print("factorial of given number is : ",ans.fact(4))
ans.pat()
ans.rev()
            