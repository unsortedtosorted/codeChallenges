class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        d={}
        d['0']='0'
        d['1']='1'
        d['8']='8'
        d['2']='5'
        d['5']='2'
        d['6']='9'
        d['9']='6'
        
        def check(num):
            temp=""
            for x in num:
                if x in d.keys():
                    temp=temp+d[x]
                else:
                    return False
            return temp!=num
            
            
        r=0
        for x in range (1,N+1):
            temp=str(x)
            if (check(temp)):
                r+=1
        
        return r
