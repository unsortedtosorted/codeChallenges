class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        r=[]
        
        
        if len(s)<1:
            return 0
        
        prev = s[0]
        i=1
        temp=1
        while i<len(s):
            if s[i]==prev:
                temp+=1
            else:
                r.append(temp)
                temp=1
                prev=s[i]
            
            i+=1
        
        r.append(temp)

        
        
        i=0
        
        temp=0
        while i+1<len(r):
            temp=temp+min(r[i],r[i+1])
            i+=1
        
        
        return temp
