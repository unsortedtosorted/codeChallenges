class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        i=0
        temp=0
        while i<len(t)-1:
            temp=temp^(ord(s[i])^ord(t[i]))
            i+=1
        temp=temp^ord(t[i])
        return (chr(temp))
