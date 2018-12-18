class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d=set()
        for i,x in enumerate(nums):
            if x in d:
                return True
            else:
                d.add(x)
            
            if len(d)>k:
                d.remove(nums[i-k])
        return False
