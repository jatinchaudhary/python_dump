def squareroot(n):

    for i in range(n//2):
        if(i*i==n):
            return i
        elif(i*i>n):
            return i-1
