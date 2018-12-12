"""
temp : [0]
temp2  [0][0][1][0][2][0][3][0]
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range (0, len(words)):
            temp=words[i]
            temp2=""
            for j in range(0,len(temp)):
                if j<len(words) and i<len(words[j]):
                    temp2=temp2+words[j][i]
                else:
                    return False
            if temp!=temp2:
                return False
        return True
                
        
        
