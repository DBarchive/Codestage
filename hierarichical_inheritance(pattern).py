class pattern:
    def oddoreven (self,n):
        return n
class oddpat(pattern):
    def odd (self):                      #hierarichical_inheritance
        for i in range (1,n+1):
            for j in range (1,i+1):
                print("*",end=' ')
            print()
class evenpat(pattern):
    def even (self):
        for i in range (1,n+1):
            for j in range (1,i+1):
                print("*",end=' ')
            print()
#main
out=oddpat()
out1=evenpat()
n=int(input("Enter the number to print the pattern :"))
if n % 2==0:
    print("The given numberer is even: ",n)
    out1.even()
else:
    print("The given number is odd :",n)
    out.odd()

            