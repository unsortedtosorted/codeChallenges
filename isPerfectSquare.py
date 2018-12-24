class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        x=1
        y=0
        while y<=num:
            if y==num:
                return True
            else:
                y+=2*x-1
                x+=1
        return False
            
