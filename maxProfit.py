class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        lastVal=prices[0]
        profit=0
        
        for x in range(1,len(prices)):
            if prices[x]>lastVal:
                profit=profit+prices[x]-lastVal
                lastVal=prices[x]
            elif prices[x]<lastVal:
                lastVal=prices[x]
                
        return profit
