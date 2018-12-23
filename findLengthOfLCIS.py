class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<1:
            return 0
        
        prev=nums[0]
        m=-sys.maxsize-1
        
        temp=1
        
        for x in range(1,len(nums)):
            
            if nums[x]>prev:
                
                temp+=1
                
            elif nums[x]<=prev:
                if temp>m:
                    m=temp
                temp=1
            prev=nums[x]
            

        if temp>m:
            m=temp
        
        if m==-sys.maxsize-1:
            return 0
        
        return m
