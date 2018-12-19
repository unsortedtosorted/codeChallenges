class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>=4:
            num=num/4
        return num==1
