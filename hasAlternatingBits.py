"""
Runs faster than 100% of python submission

check for prev bit and curr bit equality:
  if equal:
    return false
    else:
    continue
 return true

"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp=n
        
        prev=temp&1
        
        while temp!=0:
            temp=temp>>1
            next=temp&1
            if next!=prev:
                prev=next
                continue
            else:
                return False
        
        return True
