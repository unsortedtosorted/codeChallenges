
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m=0
        A.sort()
        A=A[::-1]
        for i,x in enumerate(A):
            for j,y in enumerate(A):
                for k,z in enumerate(A):
                    if i==j or i==k or j==k:
                        continue
                    if x>y+z:
                        break
                        
                    if x<y+z and y<x+z and z<x+y and x+y+z>m:
                        m=x+y+z
                        return (m)
        
        return (m)
                   
