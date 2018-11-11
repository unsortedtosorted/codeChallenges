"""
Check if a particular rotation of A
can be same as B

runs 98.83% faster than most
python submissions
"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(B)==len(A):
            return  B in A+A
        return False
