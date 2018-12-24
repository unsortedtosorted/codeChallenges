class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        A=0
        LL=1
        prev=None
        for x in s:
            if LL>2:
                return False
            if A>1:
                return False
            if x=="A":
                A+=1
                LL=1
            
            elif x=="L":
                if prev=="L":
                    LL+=1
                elif prev!="L":
                    LL=1
            
            elif x=="P":
                LL=1
            prev=x
        
        if LL>2:
            return False
        if A>1:
            return False
        
        return True 
