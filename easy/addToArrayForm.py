"""
989. Add to Array-Form of Integer


"""

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        
        carry = 0
        
        i = len(A)-1
        while i>=0 :
            x = A[i]
            k = 0
            if K > 0:
                k = K%10
                K = K//10
            
                
            
            temp = x + k + carry
            if temp > 9:
                carry = 1
                temp = temp-10
            else:
                carry = 0
            A[i] = temp
            
            i-=1
            
            
        
        if K > 0:
            while K>0:
                k = K%10
                s = k + carry
                if s>=10:
                    s = s - 10
                    carry = 1
                else:
                    carry = 0
                A = [s]+ A
                K = K//10
        
        if carry == 1:
            A = [1] + A
        
        return A
                
