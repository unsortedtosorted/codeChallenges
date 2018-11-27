class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=set(nums)
        y=list(x)
        y.sort()
        
        num=y

        
        if (len(num)-3)>=0:
            return num[len(num)-3]
        else:
            return num[len(num)-1]
        
