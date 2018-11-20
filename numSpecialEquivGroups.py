class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        d={}
        for i,v in enumerate(A):
            odd=[0]*26
            even=[0]*26
            for j,w in enumerate(v):
                if j%2==0:
                    even[ord(w)-ord('a')]+=1
                    
                else:
                    odd[ord(w)-ord('a')]+=1
            
            if str(odd+even) in d.keys():
                k=d[str(odd+even)]
                k.append(v)
                d[str(odd+even) ]=k
            else:
                d[str(odd+even) ]=[v]
                
        return len(d.keys())
