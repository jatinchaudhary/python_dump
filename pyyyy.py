n,m=input().split(" ")

a=set(input().split(" "))
b=set(input().split(" "))
c=set(input().split(" "))

hh=len(a.intersection(b))
mm=len(a.intersection(c))

print(hh-mm)
