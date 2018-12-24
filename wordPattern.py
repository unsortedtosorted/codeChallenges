class Solution:
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        p={}
        s={}
        
        p2=[]
        s2=[]
        
        num=0
        num2=0
        string=string.split(" ")
        
        if len(string)!=len(pattern):
            return False
        
        y=0
        for x in pattern:
            if x in p.keys():
                p2.append(p[x])
            else:
                p2.append(num)
                p[x]=num
                num+=1
            
            if string[y] in s.keys():
                s2.append(s[string[y]])
            else:
                s2.append(num2)
                s[string[y]]=num2
                num2+=1
            y+=1
            
        return p2==s2
