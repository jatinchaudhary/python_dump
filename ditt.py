a=int(input())

dit=0
summ=0


for i in range(a//10):
    dit=a%10
    summ+=dit
    a//=10
    if(a==0):
        a=summ        
        summ=0       
    
        
print(a)
