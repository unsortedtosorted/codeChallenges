class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s=""
        while N!=0:
            if N&1==1:
                s="1"+s
            else:
                s="0"+s
            N=N>>1
        
        
        l=-1
        r=0
        temp=0
        m=0
        
        for x,val in enumerate(s):
            if val=="0" and l!=-1:
                    r+=1
            if val=="1" and l!=-1:
                r+=1
                if r-l>=m:
                    m=r-l
                l=x
                r=x
            if val=="1" and l==-1:
                l=x
                r=x
                    
        
        return m
