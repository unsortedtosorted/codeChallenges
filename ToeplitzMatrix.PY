class Solution(object):
    def isToeplitzMatrix(self, matrix):
        
        for x in range (0,len(matrix)):
            for y in range(0,len(matrix[x])):
                if x+1>=len(matrix) or y+1>=len(matrix[x+1]):
                    continue
                if matrix[x][y]!=matrix[x+1][y+1]:
                    return False
        
        return True
