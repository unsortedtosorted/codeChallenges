
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output=[]
        for x in range(left,right+1):
            if self.selfDivide(x):
                output.append(x)
        return output
                
    def selfDivide(self,num):
        num1= str(num)
        if '0' in num1:
            return False
        
        for x in num1:
            temp=int(x)
            if num%temp!=0:
                return False
        return True
