class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return True
        
        
        first=0
        last=len(s)-1
        
        while first<=last:
            f=s[first]
            l=s[last]
            
            if not f.isalnum():
                first+=1
                continue
            if not l.isalnum():
                last-=1
                continue
            
            
            if f.lower()!=l.lower():
                return False
                
            first+=1
            last-=1
        
        return True
