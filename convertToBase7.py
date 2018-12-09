"""
7 : 10 
7/7 --> div=1, rem=0

14 : 20
14/7 --> div=2, rem=0

100: 202

100/7 --> div=14, rem=2
14/7 --> div=2 , rem=0


151:304

152/7 --> div=22, rem=4
22 --> div=3, rem=2

"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<7 and num > -7:
            return str(num)
        rem=8
        s=""
        isNeg=False
        
        if num<0:
            num=num*(-1)
            isNeg=True
            
        while num>=7:
            div=num/7
            rem=num-div*7
            num=div
            s=str(rem)+s
        
        s=str(div)+s
        if isNeg:
            s="-"+s
        return (s)
        
