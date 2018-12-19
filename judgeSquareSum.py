class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a=0
        while a*a<=c:
            b=c-a*a
            b=math.sqrt(b)
            if b==int(b):
                return True
            a+=1
        return False
