class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i=len(num1)-1
        j=len(num2)-1
        
        carry=0
        r=""
        while i>-1 or j>-1:
            temp1=0
            temp2=0
            
            if i>-1:
                temp1=ord(num1[i])-ord('0')
            if j>-1:
                temp2=ord(num2[j])-ord('0')
            
            s=temp1+temp2+carry
            
            if s>9:
                carry=1
                s=s-10
            else:
                carry=0
                s=s
            
            r=str(s)+r
            i-=1
            j-=1
          
        if carry!=0:
            r=str(carry)+r
        return (r)
            
