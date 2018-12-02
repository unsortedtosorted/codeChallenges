"""
Run time: O(N)
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        def Upper(c):
            temp=ord(c)
            
            if ord('a')<=temp<=ord('z'):
                return False
            else:
                return True
        
        
        def checkRest(word):
            last=True
            for x in range(1,len(word)):
                if Upper(word[x]):
                    last=False
            
            return last
        
        def checkRestUpper(word):
            last=True
            for x in range(1,len(word)):
                if not Upper(word[x]):
                    last=False
            
            return last
            
        
        if not Upper(word[0]):
            return checkRest(word)
        
        return checkRest(word) or checkRestUpper(word)
