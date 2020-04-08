a=list(input())
count=0
if len(a)==1:
    print(1)
else:
    for i in range(len(a)//2):
        if a[i]==a[len(a)-1-i]:
            count+=1
        else:
            break
        
    if count>0:
        print(count)
    else:
        print(-1)
