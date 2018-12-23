class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        imp=0
        sub=[id]
        
        d={}
        
        for x in employees:
            d[x.id]=x
        
        while len(sub)>0:
            y=sub.pop()
            x=d[y]
            imp+=x.importance
            sub=sub+x.subordinates
        
        return (imp)
                
"""
RunTime : O(n)
space: O(n)
"""      
