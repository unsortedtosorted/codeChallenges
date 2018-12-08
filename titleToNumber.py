class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=0
        for i,x in enumerate(s[::-1]):
            temp=temp+(ord(x)-ord('A')+1)*(math.pow(26,i))
        
        return int(temp)
            
