class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l=[]
        d=[]
        nextI=0
        nextD=len(S)
        
        for x in range(0,len(S)+1):
            d.append(x)

        if len(S)>=1:
            if S[0]=='I':
                l.append(nextI)
                d.remove(nextI)
                nextI+=1
               
            else:
                l.append(nextD)
                d.remove(nextD)
                nextD-=1
               
                

            
        for x in range(1,len(S)):
            if S[x]=='I':
                l.append(nextI)
                d.remove(nextI)
                nextI+=1
                
            else:
                l.append(nextD)
                d.remove(nextD)
                nextD-=1
                
        l.append(d[0])
        return l   
                
        
