class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d={}
        
        m=-sys.maxsize-1
        for x in deck:
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1
            
            if d[x]>m:
                m=d[x]
        
        
        r=False
        
        for x in range(2,m+1):
            for y in d:
                if d[y]%x==0:
                    r=True
                else:
                    r=False
                    break
            if r==True:
                return r
        
        return r
