
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        
        prev=nums[0]
        i=0
        
        for curr in range(1,len(nums)):
            if nums[curr]==prev:
                continue
            else:
                nums[i+1]=nums[curr]
                prev=nums[curr]
                i=i+1
        
        return (i+1)
