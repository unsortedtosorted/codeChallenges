"""
Runs 100% faster than all submissions

Check current bit: if 0, set result to true
                    if 1, set result to false and skip next bit
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        lastBit=False
        x=0
        
        while x < len(bits):
            if bits[x]==0:
                lastBit=True
            if bits[x]==1:
                lastBit=False
                x+=1
            x+=1
        return lastBit
