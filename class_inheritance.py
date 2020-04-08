class aaa:
    a=int()
    def __init__(self,a,b):
        self.a=a
        self.b=b
                      
class bbb(aaa):
    c=int()
    
    def __init__(self,c,a,b):
        self.c=c
        aaa.__init__(self,a,b)

class ccc(bbb):
    d=int()

    #def __init__(self,a,b,c,d):
     #   self.d=d
      #  bbb.__init__(self,c,a,b)

        




    
    


    
