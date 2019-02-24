class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        pit = {}
        ptm = {}
        
        for i in range(1,N+1):
            pit[i] = []
            ptm[i] = []

        for i in trust:
            
            a = i[0]
            b = i[1]
            
            ptm[b].append(a)
            pit[a].append(b)
        
        toCheck = []
        
        for i in ptm:
            if len(ptm[i]) == N-1:
                toCheck.append(i)
        
        if len(toCheck) != 1:
            return -1

        if len(pit[toCheck[0]])==0:
            return toCheck[0]
        else:
            return -1
        
