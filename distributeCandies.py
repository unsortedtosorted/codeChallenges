class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        
        kind=set(candies)
        sis=len(candies)/2
        
        if sis<=len(kind):
            return sis
        
        if sis>len(kind):
            return len(kind)
        
