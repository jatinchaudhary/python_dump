a=list(input())

b=[]



for i in range(1,len(a)+1):
    for j in range(0,len(a)-i+1):
        b.append(int(''.join(a[j:j+i])))


b=set(b)

b=list(b)
b.sort()

print(b)


for i in b:
    for j in range(i):
        print(j,end=' ')
        if j*(j+1)==i:
            print('',end=' ')
            break
    print()






