class calc:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def add(self):
        print('addtion is :',self.x + self.y)
#main
ans= calc(4,2)
ans.add()