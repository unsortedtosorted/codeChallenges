class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=0
        while n>=5:
            temp=n/5
            r=r+temp
            n=temp
        return r
            
