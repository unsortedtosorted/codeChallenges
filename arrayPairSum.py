class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum=0
        if len(nums)==1:
            return nums[0]
        x=1
        while x < len(nums):
            sum=min(nums[x-1],nums[x])+sum
            x=x+2
        return sum
