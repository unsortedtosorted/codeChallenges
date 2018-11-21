class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rowList=[]
        colList=[]
        temp=0
        
        if r*c!=len(nums)*len(nums[0]):
            return nums
        
        for row,rval in enumerate(nums):
            for cval in rval:
                colList.append(cval)
                temp+=1
                if len(colList)==c:
                    rowList.append(colList)
                    colList=[]
                    
        
        return rowList
                
