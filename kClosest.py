class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        
        def fun(p):
            x = p[0]
            y = p[1]
            
            return x*x+y*y
        
        points=sorted(points,key=fun)
        return points[:K]
