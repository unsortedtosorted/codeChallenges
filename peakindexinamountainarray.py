class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        lastMax=A[0]
        toReturn=0
        for x in range(1,len(A)):
            if lastMax<A[x]:
                lastMax=A[x]
                toReturn=x
        return toReturn
