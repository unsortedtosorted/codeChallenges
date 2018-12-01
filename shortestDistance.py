class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        val=sys.maxsize
        
        w1=-1
        w2=-1
        
        
        for i,v in enumerate(words):
            
            if v==word1:
                w1=i
            if v==word2:
                w2=i
                
            
            if w1 !=-1 and w2!=-1:
                temp=abs(w1-w2)
                if temp <val:
                    val=temp
            
        
        return val
