from itertools import permutations
j=int(input())
while(j):
    k=input().split(' ')
    num=int(k[1])
    a=list(k[0])
    a.sort()
    leng=len(a)
    h=list(permutations(a,leng))
    if leng!=len(set(h[0])):
        h=set(h)
        h=list(h)
        h.sort()

    print("".join(h[num-1]))
    j=j-1
