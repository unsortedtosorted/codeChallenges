class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        d={}
        for x in A:
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1
            if d[x]==len(A)//2:
                return x
