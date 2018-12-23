class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n>=3:
            n=n/3
            
        
        return n==1
