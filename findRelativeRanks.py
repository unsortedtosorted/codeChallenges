class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        r=sorted(nums)
        
        d={}
        for i,x in enumerate(r):
            d[x]=i+1
        
    
        r=[]
        for x in nums:
            if d[x]==len(nums):
                r.append("Gold Medal")
            elif d[x]==len(nums)-1:
                r.append("Silver Medal")
            elif d[x]==len(nums)-2:
                r.append("Bronze Medal")
            else:
                r.append(str(len(nums)-d[x]+1))
        
        return (r)   
        
