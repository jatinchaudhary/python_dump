def seq(a):

    start=1;
    for i in range(a):
        for j in range(a):
            if(j==a-1):
                print(start+j,end="")
            else:
                print(start+j,"*",end="")
        print()
        start=start+a*2
        if(i==a//2 if a%2  else i==(a//2-1)):
            start=a+1
        
