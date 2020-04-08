a=int(input())



for i in range(a):
    for j in range(a):
        if(i==j or i+j==a-1 or i+j+((a-1)//2)==(a-1)  or i+j-((a-1)//2)==(a-1) or i==(a//2)+j or j==(a//2)+i):
            print("*",end="")
        else:
            print(" ",end="")
    print();

        
        
