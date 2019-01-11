class Solution:
    def countAndSay(self, m):
        """
        :type n: int
        :rtype: str
        """
        
        
        def getseq(temp,n):
            
            prev = n[temp-1]
            
            curr=""
            last=prev[0]
            count=1
            
            for x in prev[1:]:
                
                if last==x:
                    count+=1
                    
                else:
                    curr=curr+str(count)+last
                    last=x
                    count=1
                
            curr=curr+str(count)+last
            n[temp]=curr
                        
            
            
            
            
        n = {}
        
        n[1]="1"
        n[2]="11"
        n[3]="21"
        n[4]="1211"
        n[5]="111221"
        
        
        if m<6:
            return n[m] 
        
        else:
            
            temp=5
            
            while temp!=m:
                
                getseq(temp+1,n)
                temp+=1
        
        return (n[m])
        
        
        
        
        
        
