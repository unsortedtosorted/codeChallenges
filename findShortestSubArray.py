class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        maxLen=0
        for x in range(0,len(nums)):
            if nums[x] not in d.keys():
                temp=[]
                temp.append(x)
                d[nums[x]]=temp
                if len(temp)>maxLen:
                    maxLen=len(temp)
            else:    
                temp=d[nums[x]]
                temp.append(x)
                if len(temp)>maxLen:
                    maxLen=len(temp)
                d[nums[x]]=temp

        l=[]  
        temp=0
        min=sys.maxint
        if maxLen<2:
            return maxLen
        
        for x in d.keys():
            if len(d[x])==maxLen:
                l=d[x]
                temp=l[-1]-l[0]+1
                if temp<=min:
                    min=temp
                 
        return min
