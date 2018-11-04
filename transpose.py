class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        seen=set()
        B=[]
        C=[]
        
        for  x in range (0,len(A[0])):
            for y in range (0,len(A)):
                B.append(A[y][x])
            C.append(B)
            B=[]
        return C
                
