class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=""
        for x in s.split(" "):
            r=r+x[::-1]+" "
        return r[0:len(r)-1] 
