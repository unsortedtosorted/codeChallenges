class Solution(object):
    num=0
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
       
        self.getSum(0,1,nestedList)
        return self.num
    
    def getSum(self,sum,level,item):
        
        if type(item)==list:
            for x in item:
                self.getSum(sum,level,x)
        
        elif item.isInteger():
            self.num=self.num+ item.getInteger()*(level)
        
        else:
            self.getSum(sum,level+1,item.getList())
                
  
 
