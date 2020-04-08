a=int(input())



def pattern(a,p):
    if(a>p):
        print(a," ",end="")
        pattern(a-1,p)
    else:
        return
    




def main(a,p):
    if(a>p):
        pattern(a,p)
        print()
        main(a,p+1)
    else:
        return
    


main(a,0)
                              
