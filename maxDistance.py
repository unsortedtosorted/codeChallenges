class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        #find min
        minNum=arrays[0][0]
        maxNum=arrays[0][-1]
        
        dis=-sys.maxsize-1
        
        prev=False
        
        for i in range(1,len(arrays)):
            
            
            dis=max(dis,abs(maxNum-arrays[i][0]),abs(minNum-arrays[i][-1]))
            
            minNum=min(minNum,arrays[i][0])
            maxNum=max(maxNum,arrays[i][-1])
            
            
        return dis   
                
                    
            
       
        
        
        
        
        
