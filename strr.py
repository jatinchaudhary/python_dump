a=input()



for i in range(len(a)-1,-1,-1):
    if(a[i-1]==" " or i==0):
        
        for j in range(i,len(a)):
            print(a[j],end="")
            if(a[j]==" "):
                break;
        print(" ",end="")

            
                

            
        


    
