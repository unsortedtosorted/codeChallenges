class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        for i,v in enumerate(nums):
            temp=temp^(i^nums[i])
        
        return temp^len(nums)
