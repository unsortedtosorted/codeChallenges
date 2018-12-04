class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        l1=""
        l2=""
        
        d={}
        if len(A)!=len(B):
            return False
    
        for i,v in enumerate(A):
            if v in d.keys():
                d[v]+=1
            else:
                d[v]=1
            v2=B[i]
            if v==v2:
                continue
            else:
                l1=l1+v
                l2=v2+l2
        
        
        if len(l1)==0:
            return (any( x>=2 for x in d.values()))
           
        
        if len(l1)!=2:
            return False
    

        return l1==l2
        
