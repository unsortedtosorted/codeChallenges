class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        
        d={}
        l=[]
        
        for x in A.split(" "):
            if x in d.keys():
                d[x]=d[x]+1
            else:
                d[x]=1
        
        for x in B.split(" "):
            if x not in d.keys():
                 d[x]=1
            else:
                d[x]=d[x]+1
        
        for x in d.keys():
            if d[x]==1:
                l.append(x)
        

        return l
            
