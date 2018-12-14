class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        temp=0
        r=""
        
        x=len(S)-1
        while x>-1:
            t=S[x]

            if  t.islower():
                t=t.upper()
                
            if t=="-":
                x-=1
                continue
            if t.islower():
                t=t.upper()
            
            if temp==K:    
                r=t+"-"+r
                temp=1
                x-=1
                continue
            
            if temp<K:                
                r=t+r
                temp+=1
            x-=1
                
        return r
