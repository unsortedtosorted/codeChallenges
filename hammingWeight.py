class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=1  
        flag=0
        while n!=0:
            if n&t==1:
                flag+=1
            n=n>>1
        return flag
