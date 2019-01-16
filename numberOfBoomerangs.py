"""
#447. Number of Boomerangs

"""



class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        i=0
        r=0
        while i < len(points):
            
            j=0
            d = {}
            while j<len(points):
                
                if i!=j:
                
                    dis = (points[i][0]-points[j][0])*(points[i][0]-points[j][0])+(points[i][1]-points[j][1])*(points[i][1]-points[j][1])
                    if dis in d:
                        d[dis]+=1
                    else:
                        d[dis]=1
            
                j+=1
            
            for x in d:
                if d[x]>1:
                    r+=d[x]*(d[x]-1)
            
            i+=1
            
        return r
