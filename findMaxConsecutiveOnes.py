class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        curr=0
        for x in nums:
            if x==1:
                temp+=1
            else:
                if temp>=curr:
                    curr=temp
                temp=0
        
        if temp>=curr:
            curr=temp
        return curr
