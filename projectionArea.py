class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        xy=0
        yz=0
        zx=0
        
        d={}
        
        for x in range(0,len(grid)):
            yz=max(grid[x])+yz
            for y in range(0,len(grid[x])):
                if grid[x][y]:
                    xy+=1
                if y in d.keys():
                    if grid[x][y]>d[y]:
                        zx=zx-d[y]
                        d[y]=grid[x][y]
                        zx=zx+d[y]       
                else:
                    d[y]=grid[x][y]
                    zx=zx+d[y]
                    
        return xy+yz+zx
