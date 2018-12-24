class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d={}
        
        l=[]
        m=sys.maxsize
        
        for i,x in enumerate(list1):
            d[x]=i
            
        for i,x in enumerate(list2):
            if x in d.keys():
                temp=d[x]
                s=temp+i
                if s<m:
                    l=[x]
                    m=s
                elif s==m:
                    l.append(x)
                    
        return (l)
