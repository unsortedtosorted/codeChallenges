class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        
        m={}
        x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in x:
            m[ord(i)-ord('A')]=i
            
        
        r=""
        
        while n>0:
            r=m[(n-1)%26]+r
            n=(n-1)//26
            
        
        return (r)
            
            
            
            
            
            
            
            
            
            
