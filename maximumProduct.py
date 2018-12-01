class Solution:
    s=set()
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        self.s=set()
        
        num1=(self.findMax(nums,self.s))
        self.s.add(num1)
        m=num1
        num2=(self.findMax(nums,self.s)) 
        self.s.add(num2)
        num3=(self.findMax(nums,self.s))
        p= nums[num1]*nums[num2]*nums[num3]
        self.s=set()

        p= nums[num1]*nums[num2]*nums[num3]        
        num1=(self.findMin(nums,self.s))
        self.s.add(num1)
        num2=(self.findMin(nums,self.s)) 
        self.s.add(num2)
        return max(p,nums[m]*nums[num1]*nums[num2])
    
    def findMax(self,nums,s):
            m= -sys.maxsize -1
            ind=None
            for i,x in enumerate(nums):
                if i not in self.s:
                    if x>m:
                        m=x
                        ind=i
            return ind
    
    def findMin(self,nums,s):
        
            m= sys.maxsize
            ind=None
            for i,x in enumerate(nums):
                if i not in self.s:
                    if x<m:
                        m=x
                        ind=i
            return ind
