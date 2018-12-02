class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate=licensePlate.lower()
        d={}
        for x in licensePlate:
            tempChar=x.lower()
            temp=ord(tempChar)
            
            if temp>=ord('a') and temp<=ord('z'):
                if tempChar in d.keys():
                    d[tempChar]+=1
                else:
                     d[tempChar]=1
        
        last=None
        for x in words:
            
            tempWord=x.lower()
            templ=dict(d)
            check=True
            for y in tempWord:
                if y in templ.keys():
                    templ[y]-=1

            for k in templ.keys():
                if templ[k]>0:
                    check=False
                    break
            

            if check:
                if last==None:
                    last=x
                else:
                    if len(last)>len(x):
                        last=x
        
        return last
                
                
                
                
            
        
