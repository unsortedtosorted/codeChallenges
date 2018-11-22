class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a,b,bSet= sum(A),sum(B),set(B)
        avg=(a+b)/2
        for x in A:
            if avg-a+x in bSet:
                return [x,avg-a+x]
