class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()

        while True:    
            l=str(n)
            temp=0
            for x in l:
                k=int(x)
                temp=temp+k*k
            
            if temp==1:
                return True 
            
            if temp in seen:
                return False
            else:
                seen.add(temp)
            
            n=temp
            
            
                
        
        
