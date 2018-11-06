class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num2=0
        t=1
        while num!=0:
            if num&1==0:
                num2=num2|t
            num=num>>1
            t=t<<1
        return num2 
