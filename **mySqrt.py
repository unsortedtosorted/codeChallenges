class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l=0
        r=x
        temp=(l+r)//2
        while True:
            if temp*temp==x:
                return temp
            elif temp*temp>x:
                r=temp-1
            elif temp*temp<x:
                if (temp+1)*(temp+1)>x:
                    return temp
                l=temp+1
            
            temp=(l+r)//2
