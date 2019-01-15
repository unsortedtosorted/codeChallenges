class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        
        sub = set()
        
        for x in words:
            sub.add(x)
        
       
        
        m =""
        
        for x in words:
            temp =""
            check=True
            for y in x:
                temp=temp+y
                if temp not in sub:
                    check=False
                    break
            
            if len(temp)>len(m) and check :
                m=temp
            elif len(temp)==len(m) and check:
                if temp<m:
                    m=temp
        
        return m
