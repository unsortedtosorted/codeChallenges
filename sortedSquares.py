class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        
        T = []
        
        for x in A: 
            T.append(x*x)
        
        T=sorted(T)
        
        return T
