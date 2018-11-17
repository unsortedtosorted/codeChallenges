"""
Runs faster than 77.5 to 100% python
submissions.
"""
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
        maxVal=-sys.maxint-1
        minVal=sys.maxint
        
        for x in A:
            if x>maxVal:
                maxVal=x
                
            if x<minVal:
                minVal=x
        
        diff= maxVal-minVal
        
        if diff<2*K:
            return 0
        else:
            return diff-2*K
