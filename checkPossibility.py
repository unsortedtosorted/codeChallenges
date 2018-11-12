class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        x=1
        count=0
        while x <len(nums)-1:            
            if nums[x]>=nums[x-1] and nums[x]<=nums[x+1]:
                x+=1
                continue
            
            if nums[x]<nums[x-1] and nums[x]>nums[x+1]:
                return False
            
            if nums[x-1]>nums[x]:                
                if nums[x-1]<=nums[x+1]:
                    nums[x]=nums[x-1]
                if nums[x-1]>nums[x+1]:
                    nums[x-1]=nums[x]
                x=1
                count+=1
                continue
            x+=1
        
        if count==1:
            if nums[-1]<nums[len(nums)-2]:
                return False
        
        if count>1:
            return False

        return True
