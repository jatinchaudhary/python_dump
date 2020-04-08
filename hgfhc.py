nums=list(input())
st=[]




for i in nums:
    try:
        st.remove(i)
        print("pop",i)
    except:
        print("not found",i)
        st.append(i)
        
print(st[0])
