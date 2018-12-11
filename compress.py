class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last=chars[0]
        l=0
        temp=1
        
        if len(chars)<=1:
            return len(chars)
        
        for i in range(1,len(chars)):
 
            if chars[i]==last:
                temp+=1
                continue
            else:
                last=chars[i]
                if temp==1:
                    chars[l+1]=chars[i]
                    l=l+1
                
                elif temp>1 and temp <10:
                    chars[l+1]=str(temp)
                    chars[l+2]=chars[i]
                    l=l+2
                
                elif temp>9:
                    i=1
                    for x in str(temp):
                        chars[l+i]=x
                        i+=1
                    chars[l+i]=last
                    l=l+i     
                    
                temp=1
               

        if temp>1 and temp <10:
            chars[l+1]=str(temp)
            if l+2<len(chars):
                chars[l+2]=chars[i]
        
            return (l+2)
        
        if temp>9:
            i=1
            
            for x in str(temp):
                chars[l+i]=x
                i+=1    
            return (l+i)  
            
        if temp==1:
            return (l+1)
