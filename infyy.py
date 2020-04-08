from itertools import permutations

j=int(input())

while(j):
    k=input().split(' ')

    num=int(k[1])
    a=list(k[0])

    a.sort()

    leng=len(a)

    h=list(permutations(a,leng))

    print("".join(h[num-1]))


    j=j-1


