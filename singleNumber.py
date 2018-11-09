class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        t=nums[0]
        for x in range(1,len(nums)):
            t=t^nums[x]
        return t
