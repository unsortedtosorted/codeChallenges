class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p=0
        d={}
        
        for x in range(0,len(grid)):
            for y in range(0,len(grid[x])):

                if grid[x][y]==1:
                   
                    p+=4

                    #check left
                    
                    if y-1>=0 and grid[x][y-1]==1:
                        p-=1
        
                    #check right
                    if y+1<len(grid[x]) and grid[x][y+1]==1:
                        p-=1
                    
                    #check top
                    if x-1>=0 and grid[x-1][y]==1:
                        p-=1
                   
                    #check bottom
                    if x+1<len(grid) and grid[x+1][y]==1:
                        p-=1
                                
        return p
