"""
1005. Maximize Sum Of Array After K Negations


"""


import heapq
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        m = -sys.maxsize-1
        heapq.heapify(A)
        while K>0:
            
            m = sum(A[1:])-A[0]
            K-=1
            x = heapq.heappop(A)
            heapq.heappush(A,-x)
        
        return m
            
