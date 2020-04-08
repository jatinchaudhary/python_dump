a=int(input())



def pattern(a,k):
    if(a>=k):
        print(((a*(a+1))//2)+1+k," ",end="")
        pattern(a,k+1)
    else:
        return
        



def main2(a,p):
    if(a>p):
        pattern(p,0)
        print()
        main2(a,p+1)
    else:
        return






main2(a,0)
