class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans=-sys.maxsize-1
        h1m,h2m,t1m,t2m=None,None,None,None
        for h1,h2,m1,m2 in (itertools.permutations(A)):
            h=10*h1+h2
            m=10*m1+m2
            
            if 0<=h<24 and 0<=m<60:
                t=60*h+m
                if t>ans:
                    ans=t
                    h1m,h2m,t1m,t2m=h1,h2,m1,m2
        
        if h1m==None:
            return ""
        
        else:
            return str(h1m)+str(h2m)+":"+str(t1m)+str(t2m)
