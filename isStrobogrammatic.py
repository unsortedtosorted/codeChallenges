class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        pairs = {"6": "9", "8": "8", "9": "6", "0":"0", "1":"1"}
        
        x=""
        
        
        for y in num:
            if y in pairs.keys():
                x=pairs[y]+x
            
            else:
                return False
            
        return x==num
