class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        AB=0
        AC=0
        BC=0
        area=-sys.maxsize-1
        
        for a in points:

            for b in points:
                
                if a==b:
                    continue
                for c in points:
                    if c==a or c==b:
                        continue
                    ax=(a[0]-b[0])
                    ay=(a[1]-b[1])
                    AB= ax*ax+ay*ay
                    
                    cx=(a[0]-c[0])
                    cy=(a[1]-c[1])
                    AC= cx*cx+cy*cy
                    
                    bx=(b[0]-c[0])
                    by=(b[1]-c[1])
                    BC= bx*bx+by*by 
                    
                    
                    
                    AB=math.sqrt(AB)
                    AC=math.sqrt(AC)
                    BC=math.sqrt(BC)
                    
                    
                    p=AB+BC+AC
                    p=p/2.0
                    
                    temp=p*(p-AB)*(p-AC)*(p-BC)
                    
                    if temp<0:
                        continue
                        
                    temp=math.sqrt(temp)

                    
                    if temp>area:
                        area=temp
                        
            
        return area                  
