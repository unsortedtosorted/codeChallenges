class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=set()
        r.add('a')
        r.add('e')
        r.add('i')
        r.add('o')
        r.add('u')
        
        r.add('A')
        r.add('E')
        r.add('I')
        r.add('O')
        r.add('U')
        
        l=[]
        for x in s:
            if x in r:
                l.append(x)
                
        
        p=len(l)-1
        
        r2=""
        for x in s:
            if x not in r:
                r2=r2+x
            else:

                r2=r2+l[p]
                p-=1
        
        return (r2)
