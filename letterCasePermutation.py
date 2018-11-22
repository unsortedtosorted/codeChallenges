class Solution(object):
    r=set()
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.r=set()
        self.generatePerm(S)
        self.r.add(S)
        
        return list(self.r)
        
        
    def generatePerm(self,s):
        temp=""
        for i,x in enumerate(s):
            num=ord(x)
            if num>=ord('a') and num<=ord('z'):
                if i+1<=len(s):
                    temp=s[:i]+chr(num-32)+s[i+1:]
                    if temp in self.r:
                        return
                    self.r.add(temp)
                    self.generatePerm(temp)
                    
                  
            if num>=ord('A') and num<=ord('Z'):
 
                if i+1<=len(s):
                    temp=s[:i]+chr(num+32)+s[i+1:]

                    if temp in self.r:
                        return
                    self.r.add(temp)
                    self.generatePerm(temp)
