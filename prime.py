b=4
while(b):
    b=b-1
    a=int(input("number:- "))

    m=2
    count=0

    while m<((a/2)+1):
        if(a%m==0):
            count=1
        m=m+1

    if(count==1):
        print("not prime")
    else:
        print("prime")
    
