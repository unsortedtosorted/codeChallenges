class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        
        
        n=0
        t=0
        
        while t<len(typed):
            if n==len(name):
                return True
            if name[n]==typed[t]:
                n+=1
                t+=1
            else:
                t+=1
        
        
        return n==len(name)
