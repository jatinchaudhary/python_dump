test=int(input())

ind=1


while(test):
    
    
    order=int(input())
    mat=[]
    temp=[]
    
    row=0
    col=0
    dig=0
    
    #for input
    for i in range(order):
        mat.append(input().split(" "))
        
    #for diagonal
    for i in range(order):
        dig=dig+int(mat[i][i]);
        
    
    #for row
    for i in range(order):
        if len(set(mat[i]))!=order:
            row=row+1
            
    #for column
    for i in range(order):
        for j in range(order):
            temp.append(mat[j][i])
        
        if len(set(temp))!=order:
            col=col+1
        
        temp.clear()
    
    
    
    print("Case #",ind,": ",dig,row,col)
    
    ind=ind+1
    
    temp.clear()
    mat.clear()
    
    
    
    
    test=test-1
    
    
