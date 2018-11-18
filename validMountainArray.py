class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A)<3:
            return False
        
        MaxFound=False
        prev=A[0]
        for x in range(1,len(A)-1):
            
            if A[x]==A[x+1]:
                return False
            if A[x]==A[x-1]:
                return False
            if A[x]>A[x-1] and A[x]<A[x+1]:
                continue
            if A[x]<A[x+1] and A[x]<A[x-1]:
                return False
            if A[x]>A[x-1] and A[x]>A[x+1]:
                if MaxFound==False:
                    MaxFound=True
                else:
                    return False
            

        return MaxFound
