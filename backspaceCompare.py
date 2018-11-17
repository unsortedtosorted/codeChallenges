class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.getString(S)==self.getString(T)
        
    def  getString(self,S):
        s=""
        for x in range(0,len(S)):
            if S[x]=="#":
                if x==0:
                    continue
                else:
                    s=s[:len(s)-1]
            else:
                s=s+S[x] 
        return s
