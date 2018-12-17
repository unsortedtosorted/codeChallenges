class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=1
        i=2
        
        if num<2:
            return False
        
        while i*i<num:
            if num%i==0:
                s=s+i+num/i
            i+=1
              
        return s==num
