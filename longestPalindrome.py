"""
Find the length of the longest
palindrome that can be formed

1. Iterate over string, create a dict with key=char and val=no. of repeatition
2. Now iterate over the keys,
    if val=even, add to result
    if val=odd,
        check first odd occurence
          if yes: add to result
          if not: add to result-1
          

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        l=0       
        for x in s:
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1

        notChecked=True
        
        for x in d.keys():
            if d[x]%2==0:
                l=l+d[x]
            else:
                if notChecked:
                    l=l+d[x]  
                    notChecked=False
                else:
                    l=l+d[x]-1
                    
        return l
