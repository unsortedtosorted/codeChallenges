class Solution:
    def KMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return (self.quickSelect(nums,2))
        
    def quickSelect(self,arr,k):
        piv=random.randint(0,len(arr)-1)
        small=[]
        big=[]
        
        for i,x in enumerate(arr):
            if i==piv:
                continue
            if x<arr[piv]:
                small.append(x)
            else:
                big.append(x)
        
        small.append(arr[piv])
        
        if len(small)==k:
            return small[len(small)-1]
        elif len(small)>k:
            return self.quickSelect(small,k)
        else:
            k=k-len(small)
            return self.quickSelect(big,k)
