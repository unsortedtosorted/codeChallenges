class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows==0:
            return []
        
        l=[None]*numRows
        l[0]=[1]
        if numRows==1:
            return l

        l[1]=[1,1]
        
        if numRows==2:
            return l
        
        for x in range(2,numRows):
            l[x]=[None]*(x+1)
            for y in range(0,x+1):
                if y==0 or y==x:
                    l[x][y]=1
                else:
                    l[x][y]=l[x-1][y-1]+l[x-1][y]
                    
        return (l)
