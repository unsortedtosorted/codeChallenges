class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first=0
        last=len(s)-1
        
        def checkPalindrome(s):
            f=0
            l=len(s)-1
            
            while f<l:
                if s[f]==s[l]:
                    f+=1
                    l-=1
                else:
                    return False
            return True
        
        
        
        
        while first<last:
            if s[first]==s[last]:
                first+=1
                last-=1
            else:
                if checkPalindrome(s[:first]+s[first+1:]) ==True :
                    return True
                if checkPalindrome(s[:last]+s[last+1:]) ==True:
                    return True
                return False
                
        return True
