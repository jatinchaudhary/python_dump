a=int(input())



def space(a,p):
    if(a>p):
        print(" ",end="")
        space(a,p+1)
    else:
        return



def number(p,no,measure):
    if(no>p):
        measure=1
        no=no-1

        
    if(p>no and measure==0):
        print(no,end="")
        number(p,no+1,0)
    elif(p>no and measure==1):
        print(no,end="")
        number(p,no-1,1)
    else:
        return
    
    




def pattern(a,p):
    if(p<=a):
        space(a,p)
        number(p,1,0)
        print()
        pattern(a,p+1)
    else:
        return



pattern(a,1)    


    
    

    
