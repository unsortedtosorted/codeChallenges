#Runs faster than 100% submissions


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        last=len(S)-1
        start=0
        r=list(S)
        
        while start<=last:
            if self.checkLetter(r[start]) and self.checkLetter(r[last]):

                temp=r[last]
                r[last]=r[start]
                r[start]=temp
                last-=1
                start+=1
                
            elif self.checkLetter(r[start]) and not self.checkLetter(r[last]):
                last-=1
                
            
            elif not self.checkLetter(r[start]) and self.checkLetter(r[last]):
                
                start+=1
                
            else:
                last-=1
                start+=1
            
        s="" 
        for x in r:
            s=s+x
        
        return s
            
    
    def checkLetter(self,a):
        if ord('a')<=ord(a) and ord('z')>=ord(a):
            return True
        if ord('A')<=ord(a) and ord('Z')>=ord(a):
            return True
            
        return False
