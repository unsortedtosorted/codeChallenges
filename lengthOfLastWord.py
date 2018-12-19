##Faster than 100% of online submissions
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        x=len(s)-1
        r=0
        while x>-1:
            if s[x]==" ":
                if r==0:
                    x-=1
                    continue
                else:
                    break
            else:
                r+=1
                x-=1
        return r
