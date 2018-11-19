class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
    
        if self.checkInc(A):
            return True
        else:
            return self.checkDec(A)
    
    def checkInc(self,A):
        for x,val in enumerate(A):
            if x+1<len(A):
                if A[x+1]>=A[x]:
                    continue
                else:
                    return False        
        return True
    
    def checkDec(self,A):
        for x,val in enumerate(A):
            if x+1<len(A):
                if A[x+1]<=A[x]:
                    continue
                else:
                    return False        
        return True
