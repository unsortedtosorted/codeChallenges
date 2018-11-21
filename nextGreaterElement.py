class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        l=[]
        
        for i,v in enumerate(nums):
            d[v]=i
         
        for x in findNums:
            startIndex=d[x]+1
            if startIndex>=len(nums):
                l.append(-1)
            for i in range(startIndex,len(nums)):
                if nums[i]>x:
                    l.append(nums[i])
                    break
                if i==len(nums)-1:
                    l.append(-1)              
        return l
                    
