class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l=[]
        e=[]
        for x in range (0,len(S)):
            if S[x]==C:
                e.append(x)
        
        min=1000
        temp=0
        
        for x in range(0,len(S)):
            if S[x]==C:
                l.append(0)
                continue
            for y in e:
                temp=abs(x-y)
                if temp<min:
                    min=temp
            l.append(min)
            min=1000
        
        return l
        
        
