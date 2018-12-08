class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        profit=0
        if len(prices)==0:
            return profit
        
        lastVal=prices[0]
        
        for x in range(1,len(prices)):
            profit=profit+max(0,prices[x]-lastVal)
            lastVal=prices[x]
        return profit       
                
                
            
            
            
            

            
            
                    
                    
