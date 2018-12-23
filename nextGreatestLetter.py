class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        val=ord(target)
        out=None
        
        for x in letters:
            temp=ord(x)
            if not out and temp>val:
                out=x
            elif temp>val and temp<ord(out):
                out=x

        
        if out!=None:
            return out
        
        
        for x in letters:
            temp=ord(x)
            
            if out==None:
                out=x
            
            elif val-temp>val-ord(out):
                out=x
        
        return (out)
