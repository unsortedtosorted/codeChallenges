class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        S=set()
 
        for i,v in enumerate(s):
            if i+1<len(s):
                if s[i]=='+' and s[i+1]=='+':
                    if i+2<len(s):
                        S.add(s[:i]+"--"+s[i+2:])
                    else:
                        S.add(s[:i]+"--")

        return list(S)
