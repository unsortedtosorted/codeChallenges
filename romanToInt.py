class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m={}
        m['I']=1
        m['V']=5
        m['X']=10
        m['L']=50
        m['C']=100
        m['D']=500
        m['M']=1000
        
        con=False
        v=0
        for i in range(0,len(s)):
            x=s[i]
            if con and (x=='V' or x=='L' or x=='D' or x=='X' or x=='C' or x=='M') :
                con=False
                continue
            
            if x=='I':
                if i+1<len(s):
                    if s[i+1]=='V':
                        v+=4
                        con=True
                        continue

                    
                    elif s[i+1]=='X':
                        v+=9
                        con=True
                        continue

                
                v+=1
                con=False
   
            
            elif x=='X':
                if i+1<len(s):
                    if s[i+1]=='L':
                        v+=40
                        con=True
                        continue

                        
                    
                    elif s[i+1]=='C':
                        v+=90
                        con=True
                        continue

                
                v+=10
                con=False

                    
            
            elif x=='C':
                
                if i+1<len(s):
                    if s[i+1]=='D':
                        v+=400
                        con=True
                        continue
                        
                    
                    elif s[i+1]=='M':
                        v+=900
                        con=True
                        continue

                    
                v+=100
                con=False
            
            else:
                v+=m[x]
                con=False
        
        return v
            
            
            
        
