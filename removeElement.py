class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        x=0
        lv=None
        l=len(nums)
        while x<l:
            if (nums[x] == val) :
                if lv == None:
                    lv = x
            elif nums[x] != val:
                if lv!=None:
                    temp1=nums[x]
                    temp2=nums[lv]
                    nums[x]=temp2
                    nums[lv]=temp1
                    x=lv
                    lv=None
            x+=1
        
        
        if lv==None:
            return len(nums)
        else:
            return lv
        
