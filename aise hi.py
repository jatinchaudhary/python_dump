class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        finalll=[]
        temp=[]
        
        hk=strs.copy()
        while len(strs)!=0:
            k=0
            lastchk=0
            temp.clear()
        
            for i in strs:
                k+=1
                chk=list(i)
                chk.sort()
                if k==1:
                    lastchk=chk
            
                if lastchk==chk:
                    temp.append(i)
                    hk.remove(i)        
            finalll.append(temp.copy())
            strs=hk.copy()
        return finalll
