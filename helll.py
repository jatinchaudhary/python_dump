a=input()

a=list(map(int,a.split(',')))

chk=0
summ=0
sum1=[]

for i in range(len(a)):
    if a[i]!=5:
        summ=summ+a[i]
    else:
        break
    
for i in range(len(a)-1,-1,-1):
    if a[i]!=8:
        summ=summ+a[i]
    else:
        break




for i in range(len(a)):

    if a[i]==5:
        chk=1

    if a[i]==8:
        chk=0
    
    if chk==1 and a[i]!=5:
        sum1.append(str(a[i]))
    


print(summ)
print(sum1)






