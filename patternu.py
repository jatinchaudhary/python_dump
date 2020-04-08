def pat(n,a):
    i=a
    while i<=n:
        print(i," ",end="")
        i+=1
    print()
    if(a!=0):
        pat(n,a-1)
        i=a
        while i<=n:
            print(i," ",end="")
            i+=1
        print()
        
def patt(n):
    pat(n,n)

    
        
        
        
