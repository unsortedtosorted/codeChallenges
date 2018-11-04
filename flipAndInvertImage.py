class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for x in range(0,len(A)):
            temp=A[x]
            A[x]=temp[::-1]
            
        for x in range(0,len(A)):
            for y in range(0,len(A[x])):
                if A[x][y]==1:
                    A[x][y]=0
                else:
                    A[x][y]=1
        return A
