
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        
        heapq.heapify(nums)
        self.nums=nums
        self.k=k
        while len(self.nums)>k:
            heapq.heappop(self.nums)
        
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        heapq.heappush(self.nums,val)
        
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        
        return self.nums[0]
            
