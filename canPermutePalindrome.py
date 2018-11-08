"""
In Palindrone all characters should appear even times, 
expect one character that is allowed to appear odd number of time

Faster than 98.85% of Python
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d={}
        for x in s:
            if x not in d.keys():
                d[x]=1
            else:
                d[x]+=1
        
        odd=0
        for x in d.values():
            if x%2==0:
                continue
            else:
                if odd==0:
                    odd=1
                else:
                    return False
        return True
