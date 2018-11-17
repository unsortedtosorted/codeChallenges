class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        r=""
        S=S.split(" ")
        v=['a','A','e','E','i','I','o','O','u','U']
        a=""
        for x in S:
            a=a+"a"
            if x[0] in v:
                temp=x+"ma"
                temp=temp+a
                r=r+temp+" "
            else:
                temp=x[1:]+x[0]+"ma"
                temp=temp+a
                r=r+temp+" "
        
        return r[0:len(r)-1]
