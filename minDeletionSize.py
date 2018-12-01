class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        if len(A)<1:
            return None
        
        r=len(A)
        c=len(A[0])
        
        d=[]
        prev=sys.maxsize
        for col in range(0,c):
            for row in range(0,r):
                
                if row==0:
                    prev=ord(A[row][col])
                    continue
                else:
                    curr=ord(A[row][col])
                    if curr<prev:
                        d.append(col)
                        break
                    prev=curr
        return len(d)
                    
                    
