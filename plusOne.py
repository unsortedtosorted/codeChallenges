class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        x=len(digits)-1
        k=digits[x]
        
        s=k+1
        
        if s<=9:
            digits[x]=s
            carry=0
        else:
            carry=1
            digits[x]=s-10
            
            k=x-1
            
            while k>-1:
                if carry==1:
                    s=digits[k]+carry
                    if s<=9:
                        digits[k]=s
                        carry=0
                    else:
                        carry=1
                        digits[k]=s-10
                        k-=1
                else:
                    break
                        
        
        if carry!=0:
            digits=[1]+digits
                
        return digits
