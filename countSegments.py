"""

Faster than 100% online submissions
"""
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        
        if len(s)<1:
            return 0
        prev= " "==s[0]

        for x in range(1,len(s)):
            if not prev and s[x]==" ":
                i+=1
                prev=True
            elif s[x]!=" ":
                prev=False
                
        if prev:
            return i
        else:return (i+1)
