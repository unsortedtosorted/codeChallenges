class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lastEven=0
        lastOdd=1
        B=[None]*len(A)
        
        for x in range(0,len(A)):
            if A[x]%2 == 0:
                B[lastEven]=A[x]
                lastEven+=2    
            else:
                B[lastOdd]=A[x]
                lastOdd+=2
        
        return B
